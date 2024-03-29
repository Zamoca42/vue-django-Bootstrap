def obj_to_post(obj, flag=True):
    """
    obj의 각 속성을 serialize 해서, dict로 변환한다.
    serialize: python object --> (기본 타입) int, float, str
    :param obj:
    :param flag: True (모두 보냄, /api/post/99/ 용), False (일부 보냄, /api/post/list/ 용)
    :return;
    """
    post = dict(vars(obj))

    if obj.category:
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'
    
    # = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = 'https://via.placeholder.com/900x300/'

    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime('%B %d, %Y')
    else:
        post['modify_dt'] = 'Not Update Yet'
    
    # = models.DateTimeField('MODIFY DATE', auto_now=True)

    del post['_state'], post['category_id'], post['create_dt']
    if not flag:
        del post['modify_dt'], post['description'], post['content']
    return post

def prev_next_post(obj):
    try:
        prevObj = obj.get_previous_by_modify_dt()
        prevDict = {
            'id': prevObj.id,
            'title': prevObj.title,
        }
    except obj.DoesNotExist:
        prevDict = {}
    
    try:
        nextObj = obj.get_next_by_modify_dt()
        nextDict = {
            'id': nextObj.id,
            'title': nextObj.title,
        }
    except obj.DoesNotExist:
        nextDict = {}

    return prevDict, nextDict
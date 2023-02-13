def obj_to_post(obj):
    """
    obj의 각 속성을 serialize 해서, dict로 변환한다.
    serialize: python object --> (기본 타입) int, float, str
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
        post['image'] = 'https://via.placeholder.com/900x400/'

    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime('%B %d, %Y')
    else:
        post['modify_dt'] = 'Not Update Yet'
    
    # = models.DateTimeField('MODIFY DATE', auto_now=True)

    del post['_state'], post['category_id'], post['create_dt']
    return post
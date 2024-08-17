from sqlmodel import Session, select, or_


def get_by_dict(engine, model, query_dict: dict):
    """
    根据查询字典指定的键值对等值查询数据
    :param engine: 引擎对象
    :param model: 模型类
    :param query_dict: 查询字典
    """
    with Session(engine) as session:
        query = select(model)
        if isinstance(query_dict, dict):
            for k, v in query_dict.items():
                if hasattr(model, k):
                    query = query.where(getattr(model, k) == v)
        results = session.exec(query)
        return results.all()


def get_by_dict_or(engine, model, query_dict: dict):
    """
    根据查询字典指定的键值对查询数据，键值对之间的关系是or的关系
    :param engine: 引擎对象
    :param model: 模型类
    :param query_dict: 查询字典 {age:{gt:3,lt:33}}
    """
    with Session(engine) as session:
        query = select(model)
        if isinstance(query_dict, dict):
            for k, v in query_dict.items():
                if hasattr(model, k):
                    if isinstance(v, dict):
                        # or_(Hero.age <= 35, Hero.age > 90)
                        mk = getattr(model, k)
                        conditions = []
                        for kk, vv in v.items():
                            if kk == "==":
                                conditions.append(mk == vv)
                            elif kk == ">":
                                conditions.append(mk > vv)
                            elif kk == "<":
                                conditions.append(mk < vv)
                            elif kk == ">=":
                                conditions.append(mk >= vv)
                            elif kk == "<=":
                                conditions.append(mk <= vv)
                        query = query.where(or_(*conditions))
        results = session.exec(query)
        return results.all()


def get_by_dict_and(engine, model, query_dict: dict):
    """
    根据查询字典指定的键值对查询数据，键值对之间的关系是and的关系
    :param engine: 引擎对象
    :param model: 模型类
    :param query_dict: 查询字典 {age:{gt:3,lt:33}}
    """
    with Session(engine) as session:
        query = select(model)
        if isinstance(query_dict, dict):
            for k, v in query_dict.items():
                if hasattr(model, k):
                    if isinstance(v, dict):
                        # or_(Hero.age <= 35, Hero.age > 90)
                        mk = getattr(model, k)
                        conditions = []
                        for kk, vv in v.items():
                            if kk == "==":
                                conditions.append(mk == vv)
                            elif kk == ">":
                                conditions.append(mk > vv)
                            elif kk == "<":
                                conditions.append(mk < vv)
                            elif kk == ">=":
                                conditions.append(mk >= vv)
                            elif kk == "<=":
                                conditions.append(mk <= vv)
                        query = query.where(*conditions)
        results = session.exec(query)
        return results.all()


def get_all(engine, model):
    """
    查询所有数据
    :param engine: 引擎对象
    :param model: 模型类
    """
    with Session(engine) as session:
        return session.exec(select(model)).all()

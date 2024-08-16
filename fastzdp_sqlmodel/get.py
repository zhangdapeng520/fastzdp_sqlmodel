from sqlmodel import Session, select


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
                query = query.where(getattr(model, k) == v)
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

from sqlmodel import Session, select, func


def get_sum(engine, model, column):
    """
    获取求和结果
    :param engine 引擎对象
    :param model 模型对象
    :param column 要求和的列明
    """
    if not hasattr(model, column):
        return 0
    total = 0
    with Session(engine) as session:
        query = select(func.sum(getattr(model, column)))
        result = session.exec(query).one()
        total = float(result) if result else 0
    return total

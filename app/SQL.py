from sqlmodel import create_engine


def get_engine():
    """
    Get the database engine

    Parameters
    ----------

    Returns
    -------
    Engine : database engine
    """
    return create_engine("sqlite:///database/database.db", echo=True)


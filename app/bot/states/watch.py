from aiogram.fsm.state import State, StatesGroup


class WatchFlightState(StatesGroup):

    origin = State()
    destination = State()
    date_from = State()
    date_to = State()
    max_price = State()

from model import DesignPattern
import view


def show_all():
    patterns = DesignPattern.getAll()
    return view.show_all(patterns)


def start():
    view.start()
    user_input = input('')
    if user_input == 'y':
        return show_all()
    else:
        return view.end()


if __name__ == '__main__':
    start()

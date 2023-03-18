from main import BooksCollector

class TestBooksCollector:

    def test_books_rating_is_empty(self):
        collector_1 = BooksCollector()
        assert collector_1.books_rating == {} # проверка, что словарь books_rating изначально пустой

    def test_favorites_is_empty(self):
        collector_2 = BooksCollector()
        assert collector_2.favorites == [] # проверка, что список favorites изначально пустой

    def test_add_new_book_add_two_books(self):
        collector_3 = BooksCollector()
        collector_3.add_new_book('Гордость и предубеждение и зомби')
        collector_3.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector_3.get_books_rating() == {'Гордость и предубеждение и зомби': 1,'Что делать, если ваш кот хочет вас убить': 1} # проверка, что в словарь books_rating добавились правильные книги

    def test_add_new_book_add_existing_book(self):
        collector_4 = BooksCollector()
        collector_4.add_new_book('A Byte of Python')
        collector_4.add_new_book('A Byte of Python')
        assert collector_4.get_books_rating() == {'A Byte of Python': 1} # проверка, что в словарь books_rating нельзя повторно добавить существующую в словаре книгу

    def test_set_book_rating_set_new_rating(self):
        collector_5 = BooksCollector()
        collector_5.add_new_book('A Byte of Python')
        collector_5.set_book_rating('A Byte of Python', 10)
        assert collector_5.get_books_rating() == {'A Byte of Python': 10} # проверка, что можно установить новый рейтинг добавленной в словарь books_rating книге

    def test_set_book_rating_set_rating_for_nonexistent_book(self):
        collector_6 = BooksCollector()
        collector_6.add_new_book('A Byte of Python')
        collector_6.set_book_rating('Atlas Shrugged', 2)
        assert collector_6.get_books_rating() == {'A Byte of Python': 1} # проверка, что несуществующей книге в словаре books_rating нельзя установить рейтинг

    def test_set_book_rating_set_rating_less_than_1(self):
        collector_7 = BooksCollector()
        collector_7.add_new_book('A Byte of Python')
        collector_7.set_book_rating('A Byte of Python', 0)
        assert collector_7.get_books_rating() == {'A Byte of Python': 1} # проверка, что добавленной в словарь books_rating книге нельзя установить рейтинг меньше 1

    def test_set_book_rating_set_rating_less_more_10(self):
        collector_8 = BooksCollector()
        collector_8.add_new_book('A Byte of Python')
        collector_8.set_book_rating('A Byte of Python', 11)
        assert collector_8.get_books_rating() == {'A Byte of Python': 1}  # проверка, что добавленной в словарь books_rating книге нельзя установить рейтинг больше 10

    def test_get_book_rating_check_book_raiting(self):
        collector_9 = BooksCollector()
        collector_9.add_new_book('A Byte of Python')
        collector_9.set_book_rating('A Byte of Python', 10)
        assert collector_9.get_book_rating('A Byte of Python') == 10 # проверка измененного рейтинга у добавленной книги

    def test_get_book_rating_nonexistent_book_has_no_raiting(self):
        collector_10 = BooksCollector()
        nonexistent_book = collector_10.get_book_rating('Atlas Shrugged')
        assert nonexistent_book == None # проверка, что у не добавленной книги нет рейтинга

    def test_get_books_with_specific_rating_get_list_of_books(self):
        collector_11 = BooksCollector()
        collector_11.add_new_book('A Byte of Python')
        collector_11.add_new_book('Atlas Shrugged')
        assert collector_11.get_books_with_specific_rating(1) == ['A Byte of Python', 'Atlas Shrugged'] # проверка, что выводится список книг с рейтингом 1

    def test_get_books_rating_get_dict_books_rating(self):
        collector_12 = BooksCollector()
        collector_12.add_new_book('A Byte of Python')
        assert collector_12.get_books_rating() == {'A Byte of Python': 1} # проверка вывода словаря books_rating с добавленной книгой

    def test_add_book_in_favorites_add_book_in_favorites_list(self):
        collector_13 = BooksCollector()
        collector_13.add_new_book('A Byte of Python')
        collector_13.add_book_in_favorites('A Byte of Python')
        assert collector_13.favorites == ['A Byte of Python'] # проверка добавления книги в список избранных — favorites

    def test_add_book_in_favorites_add_existing_book_in_favorites_list(self):
        collector_14 = BooksCollector()
        collector_14.add_new_book('A Byte of Python')
        collector_14.add_new_book('Atlas Shrugged')
        collector_14.add_book_in_favorites('A Byte of Python')
        collector_14.add_book_in_favorites('Atlas Shrugged')
        collector_14.add_book_in_favorites('A Byte of Python')
        assert collector_14.favorites == ['A Byte of Python', 'Atlas Shrugged'] # проверка, что нельзя повторно добавить книгу в список избранных — favorites

    def test_add_book_in_favorites_add_nonexistent_book_in_favorites_list(self):
        collector_15 = BooksCollector()
        collector_15.add_book_in_favorites('A Byte of Python')
        assert collector_15.favorites == [] # проверка, что нельзя добавить книгу в избранное, если её нет в словаре books_rating

    def test_delete_book_from_favorites_delete_existing_book(self):
        collector_16 = BooksCollector()
        collector_16.add_new_book('A Byte of Python')
        collector_16.add_book_in_favorites('A Byte of Python')
        collector_16.delete_book_from_favorites('A Byte of Python')
        assert collector_16.favorites == [] # проверка удаления добавленной книги из списка избранных

    def test_delete_book_from_favorites_delete_nonexistent_book(self):
        collector_17 = BooksCollector()
        collector_17.delete_book_from_favorites('Atlas Shrugged')
        assert collector_17.favorites == [] # проверка удаления книги, отсутствующей в списке избранного — favorites

    def test_get_list_of_favorites_books_get_list(self):
        collector_18 = BooksCollector()
        collector_18.add_new_book('A Byte of Python')
        collector_18.add_new_book('Atlas Shrugged')
        collector_18.add_book_in_favorites('A Byte of Python')
        collector_18.add_book_in_favorites('Atlas Shrugged')
        assert collector_18.get_list_of_favorites_books() == ['A Byte of Python', 'Atlas Shrugged'] # проверка получения списка избранных


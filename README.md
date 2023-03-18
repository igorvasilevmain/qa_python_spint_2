Реализованные тесты:

1) test_books_rating_is_empty — проверка, что словарь books_rating изначально пустой
2) test_favorites_is_empty — проверка, что список favorites изначально пустой
3) test_add_new_book_add_two_books — проверка, что в словарь books_rating добавились правильные книги
4) test_add_new_book_add_existing_book — проверка, что в словарь books_rating нельзя повторно добавить существующую в словаре книгу
5) test_set_book_rating_set_new_rating — проверка, что можно установить новый рейтинг добавленной в словарь books_rating книге
6) test_set_book_rating_set_rating_for_nonexistent_book — проверка, что несуществующей книге в словаре books_rating нельзя установить рейтинг
7) test_set_book_rating_set_rating_less_than_1 — проверка, что добавленной в словарь books_rating книге нельзя установить рейтинг меньше 1
8) test_set_book_rating_set_rating_less_more_10 — проверка, что добавленной в словарь books_rating книге нельзя установить рейтинг больше 10
9) test_get_book_rating_check_book_raiting — проверка измененного рейтинга у добавленной книги
10) test_get_book_rating_nonexistent_book_has_no_raiting — проверка, что у не добавленной книги нет рейтинга
11) test_get_books_with_specific_rating_get_list_of_books — проверка, что выводится список книг с рейтингом 1
12) test_get_books_rating_get_dict_books_rating — проверка вывода словаря books_rating с добавленной книгой
13) test_add_book_in_favorites_add_book_in_favorites_list — проверка добавления книги в список избранных — favorites
14) test_add_book_in_favorites_add_existing_book_in_favorites_list — проверка, что нельзя повторно добавить книгу в список избранных — favorites
15) test_add_book_in_favorites_add_nonexistent_book_in_favorites_list — проверка, что нельзя добавить книгу в избранное, если её нет в словаре books_rating
16) test_delete_book_from_favorites_delete_existing_book — проверка удаления добавленной книги из списка избранных
17) test_delete_book_from_favorites_delete_nonexistent_book — проверка удаления книги, отсутствующей в списке избранного — favorites
18) test_get_list_of_favorites_books_get_list — проверка получения списка избранных



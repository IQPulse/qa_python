import pytest
class TestBooksCollector:

    @pytest.mark.parametrize("book_name, expected_result", [("Гордость и предубеждение и зомби", 1),
                                                           ("Что делать, если ваш кот хочет вас убить", 1)])
    def test_add_new_book(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_result

    @pytest.mark.parametrize("book_name, genre, expected_result", [("Гордость и предубеждение и зомби", "Фантастика", "Фантастика"),
                                                                   ("Что делать, если ваш кот хочет вас убить", "Комедии", "Комедии")])
    def test_set_book_genre(self, collector, book_name, genre, expected_result):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_result

    @pytest.mark.parametrize("book_name, genre", [("Гордость и предубеждение и зомби", "Фантастика"),
                                                  ("Что делать, если ваш кот хочет вас убить", "Комедии")])
    def test_get_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("genre, expected_result", [("Фантастика", ["Гордость и предубеждение и зомби"]),
                                                       ("Комедии", ["Что делать, если ваш кот хочет вас убить"])])
    def test_get_books_with_specific_genre(self, collector, genre, expected_result):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Комедии")
        assert collector.get_books_with_specific_genre(genre) == expected_result

    @pytest.mark.parametrize("book_name1, genre1, book_name2, genre2", [("Гордость и предубеждение и зомби", "Фантастика", "Что делать, если ваш кот хочет вас убить", "Комедии")])
    def test_get_books_genre(self, collector, book_name1, genre1, book_name2, genre2):
        collector.add_new_book(book_name1)
        collector.add_new_book(book_name2)
        collector.set_book_genre(book_name1, genre1)
        collector.set_book_genre(book_name2, genre2)
        assert collector.get_books_genre() == {book_name1: genre1, book_name2: genre2}

    @pytest.mark.parametrize("book_name1, genre1, book_name2, genre2, expected_result", [("Гордость и предубеждение и зомби", "Фантастика", "Что делать, если ваш кот хочет вас убить", "Комедии", ["Что делать, если ваш кот хочет вас убить"])])
    def test_get_books_for_children(self, collector, book_name1, genre1, book_name2, genre2, expected_result):
        collector.add_new_book(book_name1)
        collector.add_new_book(book_name2)
        collector.set_book_genre(book_name1, genre1)
        collector.set_book_genre(book_name2, genre2)
        assert collector.get_books_for_children() == expected_result

    @pytest.mark.parametrize("book_name, expected_result", [("Гордость и предубеждение и зомби", ["Гордость и предубеждение и зомби"])])
    def test_add_book_in_favorites(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected_result

    @pytest.mark.parametrize("book_name, expected_result", [("Гордость и предубеждение и зомби", []), ("Что делать, если ваш кот хочет вас убить", [])])
    def test_delete_book_from_favorites(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == expected_result

    @pytest.mark.parametrize("book_name1, expected_result", [("Гордость и предубеждение и зомби", ["Гордость и предубеждение и зомби"]),
                                                             ("Что делать, если ваш кот хочет вас убить", ["Что делать, если ваш кот хочет вас убить"])])
    def test_get_list_of_favorites_books(self, collector, book_name1, expected_result):
        collector.add_new_book(book_name1)
        collector.add_book_in_favorites(book_name1)
        assert collector.get_list_of_favorites_books() == expected_result

    @pytest.mark.parametrize("book_name, genre, expected_result", [("Скажи ей, что она красива", "Мелодрама", ["Скажи ей, что она красива"])])
    def test_books_with_age_rating_not_for_children(self, collector, book_name, genre, expected_result):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == expected_result

    @pytest.mark.parametrize("book_name, expected_result", [("Тестовая книга", "")])
    def test_get_genre_for_book_without_genre(self, collector, book_name, expected_result):
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == expected_result

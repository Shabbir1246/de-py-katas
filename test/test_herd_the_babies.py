from src.herd_the_babies.herd_the_babies import *

class TestHerdTheBabies:

    def test_should_return_the_argument_unaltered_if_no_matching_upper_and_lower_case_letters_found(self):
        """ parent is a capital letter and child is same letter in lower case """
        # Arrange
        test_herd = "aa"

        # ACT
        result = herd_the_babies(test_herd)
        # print (sorted("DbbaeaccAC"))

        # Assert
        assert result == "aa"

    def test_should_return_a_sorted_list_of_parent_followed_by_its_children(self):
        # Arrange
        test_herd = "aBA"

        # ACT
        result = herd_the_babies(test_herd)

        # Assert
        assert result == "AaB"

    def test_should_return_a_sorted_list_of_parent_followed_by_its_children_and_then_all_orphans(self):
        # Arrange
        test_herd = "DbbaeaccAC"

        # ACT
        result = herd_the_babies(test_herd)

        # Assert
        assert result == "AaaCccDbbe"
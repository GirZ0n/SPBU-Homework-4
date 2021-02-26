import unittest
from homework.homework1.task1.matrix import Matrix


class MatrixTestCase(unittest.TestCase):
    def test_constructor_zero_length(self):
        with self.assertRaises(ValueError) as context:
            Matrix()

        self.assertTrue("Matrix must contain at least one element." in str(context.exception))

    def test_constructor_different_length(self):
        with self.assertRaises(ValueError) as context:
            Matrix([733, 83, 15], [365, 119, 789], [173])

        self.assertTrue("Matrix rows must be the same length." in str(context.exception))

    def test_equality_equal_columns(self):
        m1 = Matrix([987], [233], [929])
        m2 = Matrix([987], [233], [929])

        self.assertEqual(m1, m2)

    def test_equality_unequal_columns(self):
        m1 = Matrix([987], [233], [929])
        m2 = Matrix([270], [811], [37])

        self.assertNotEqual(m1, m2)

    def test_equality_equal_rows(self):
        m1 = Matrix([43, 492, 363, 846, 274])
        m2 = Matrix([43, 492, 363, 846, 274])

        self.assertEqual(m1, m2)

    def test_equality_unequal_rows(self):
        m1 = Matrix([823, 336, 626, 171, 193])
        m2 = Matrix([788, 427, 809, 809, 193])

        self.assertNotEqual(m1, m2)

    def test_equality_equal_matrices(self):
        m1 = Matrix([997, 367, 422, 894, 825], [976, 645, 384, 984, 839], [31, 609, 456, 641, 986])
        m2 = Matrix([997, 367, 422, 894, 825], [976, 645, 384, 984, 839], [31, 609, 456, 641, 986])

        self.assertEqual(m1, m2)

    def test_equality_unequal_matrices(self):
        m1 = Matrix([510, 546, 67, 502, 481], [18, 268, 315, 192, 319], [801, 935, 50, 787, 143])
        m2 = Matrix([255, 75, 734, 591, 496], [268, 307, 258, 397, 155], [901, 369, 148, 61, 464])

        self.assertNotEqual(m1, m2)

    def test_add_columns_same_dimension(self):
        m1 = Matrix([959], [362], [717])
        m2 = Matrix([941], [195], [242])

        expected = Matrix([959 + 941], [362 + 195], [717 + 242])
        self.assertEqual(m1 + m2, expected)

    def test_add_columns_different_dimension(self):
        m1 = Matrix([526], [685], [590], [991])
        m2 = Matrix([333])

        with self.assertRaises(ValueError) as context:
            m1 + m2

        self.assertTrue("Matrices do not have the same dimensions." in str(context.exception))

    def test_add_rows_same_dimension(self):
        m1 = Matrix([95, 891, 184, 714, 107])
        m2 = Matrix([470, 327, 596, 684, 350])

        expected = Matrix([95 + 470, 891 + 327, 184 + 596, 714 + 684, 107 + 350])
        self.assertEqual(m1 + m2, expected)

    def test_add_rows_different_dimension(self):
        m1 = Matrix([91, 862, 916, 489, 48])
        m2 = Matrix([19, 218, 287])

        with self.assertRaises(ValueError) as context:
            m1 + m2

        self.assertTrue("Matrices do not have the same dimensions." in str(context.exception))

    def test_add_matrices_same_dimension(self):
        m1 = Matrix([238, 92, 882, 828, 414], [859, 686, 277, 658, 975])
        m2 = Matrix([85, 356, 292, 110, 409], [571, 701, 712, 737, 738])

        expected = Matrix(
            [238 + 85, 92 + 356, 882 + 292, 828 + 110, 414 + 409],
            [859 + 571, 686 + 701, 277 + 712, 658 + 737, 975 + 738],
        )
        self.assertEqual(m1 + m2, expected)

    def test_add_matrices_different_dimension(self):
        m1 = Matrix([124, 97, 408, 760, 407], [563, 209, 568, 79, 645])
        m2 = Matrix([497, 75, 816, 275, 383])

        with self.assertRaises(ValueError) as context:
            m1 + m2

        self.assertTrue("Matrices do not have the same dimensions." in str(context.exception))

    def test_mul_row_and_column_compatible(self):
        m1 = Matrix([786, 892, 641, 53, 989])
        m2 = Matrix([82], [834], [335], [908], [540])

        expected = Matrix([786 * 82 + 892 * 834 + 641 * 335 + 53 * 908 + 989 * 540])

        self.assertEqual(m1 * m2, expected)

    def test_mul_row_and_column_incompatible(self):
        m1 = Matrix([740, 34, 117, 867, 348])
        m2 = Matrix([1], [2])

        with self.assertRaises(ValueError) as context:
            m1 * m2

        self.assertTrue("Matrices have incompatible dimensions." in str(context.exception))

    def test_mul_compatible_matrices(self):
        m1 = Matrix([672, 759, 235, 419, 281], [546, 963, 866, 216, 490])
        m2 = Matrix([768, 756], [228, 744], [384, 864], [424, 863], [605, 142])

        expected = Matrix([1127049, 1677267], [1359470, 2133460])

        self.assertEqual(m1 * m2, expected)

    def test_mul_incompatible_matrices(self):
        m1 = Matrix([108, 463, 982, 620, 339], [395, 69, 198, 571, 568])
        m2 = Matrix([35, 942, 279, 9, 894])

        with self.assertRaises(ValueError) as context:
            m1 * m2

        self.assertTrue("Matrices have incompatible dimensions." in str(context.exception))

    def test_transpose_column(self):
        m = Matrix([280], [344], [193], [46], [264])

        expected = Matrix([280, 344, 193, 46, 264])

        self.assertEqual(m.transpose(), expected)

    def test_transpose_row(self):
        m = Matrix([160, 364, 410, 855, 686])

        expected = Matrix([160], [364], [410], [855], [686])

        self.assertEqual(m.transpose(), expected)

    def test_transpose_matrix(self):
        m = Matrix([797, 199, 712, 986, 58], [392, 839, 559, 396, 713], [579, 841, 427, 959, 590])

        expected = Matrix([797, 392, 579], [199, 839, 841], [712, 559, 427], [986, 396, 959], [58, 713, 590])

        self.assertEqual(m.transpose(), expected)

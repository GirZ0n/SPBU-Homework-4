import unittest
from homework.homework1.task1.matrix import Matrix


class IntegerMatrixTestCase(unittest.TestCase):
    def test_constructor_zero_length(self):
        with self.assertRaises(ValueError) as context:
            Matrix()

        self.assertTrue("Matrix must contain at least one element." in str(context.exception))

    def test_constructor_zero_length_rows(self):
        with self.assertRaises(ValueError) as context:
            Matrix([], [])

        self.assertTrue("Matrix rows must not be empty." in str(context.exception))

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


class FloatMatrixTestCase(unittest.TestCase):
    def test_constructor_different_length(self):
        with self.assertRaises(ValueError) as context:
            Matrix([166.8932, -873.1473, -846.3777], [-290.3968, -969.3996, -402.5956], [-965.0912])

        self.assertTrue("Matrix rows must be the same length." in str(context.exception))

    def test_equality_equal_columns(self):
        m1 = Matrix([588.9390], [307.9836], [385.3508])
        m2 = Matrix([588.9390], [307.9836], [385.3508])

        self.assertEqual(m1, m2)

    def test_equality_unequal_columns(self):
        m1 = Matrix([-972.7679], [25.0111], [439.4697])
        m2 = Matrix([-634.7300], [481.6297], [-61.8749])

        self.assertNotEqual(m1, m2)

    def test_equality_equal_rows(self):
        m1 = Matrix([-766.4959, 936.0211, 93.3980, -661.5449, 71.8693])
        m2 = Matrix([-766.4959, 936.0211, 93.3980, -661.5449, 71.8693])

        self.assertEqual(m1, m2)

    def test_equality_unequal_rows(self):
        m1 = Matrix([-89.1880, 988.0237, 790.8019, 550.1498, 466.6292])
        m2 = Matrix([-907.6041, -292.5741, 321.8467, -48.7934, -362.5269])

        self.assertNotEqual(m1, m2)

    def test_equality_equal_matrices(self):
        m1 = Matrix(
            [881.0386, -97.0578, 315.7350, -178.2707, 514.3505],
            [-469.0618, -968.7969, -156.4953, -391.3473, -236.1674],
            [-67.7664, 385.8665, -839.8274, 844.9972, -585.4969],
        )
        m2 = Matrix(
            [881.0386, -97.0578, 315.7350, -178.2707, 514.3505],
            [-469.0618, -968.7969, -156.4953, -391.3473, -236.1674],
            [-67.7664, 385.8665, -839.8274, 844.9972, -585.4969],
        )

        self.assertEqual(m1, m2)

    def test_equality_unequal_matrices(self):
        m1 = Matrix(
            [-713.8768, 810.2739, -55.4427, -2.1501, 347.9285],
            [-807.1974, -278.7502, 744.8431, -713.6801, 97.8125],
            [885.1824, 252.8629, -178.6706, -378.5227, -409.2536],
        )
        m2 = Matrix(
            [211.0487, -893.6526, 881.1875, -495.1150, 247.5286],
            [-381.6731, 715.2943, 144.4056, -298.4180, 536.6270],
            [-893.5463, -150.7979, -849.2471, 598.2600, -809.2685],
        )

        self.assertNotEqual(m1, m2)

    def test_add_columns_same_dimension(self):
        m1 = Matrix([570.6692], [-418.9927], [676.4275])
        m2 = Matrix([-647.6599], [-621.8909], [934.6862])

        expected = Matrix([570.6692 + -647.6599], [-418.9927 + -621.8909], [676.4275 + 934.6862])
        self.assertEqual(m1 + m2, expected)

    def test_add_columns_different_dimension(self):
        m1 = Matrix([530.4039], [-134.8317], [473.0600], [-321.8502])
        m2 = Matrix([-309.7991])

        with self.assertRaises(ValueError) as context:
            m1 + m2

        self.assertTrue("Matrices do not have the same dimensions." in str(context.exception))

    def test_add_rows_same_dimension(self):
        m1 = Matrix([477.0836, -26.9211, -23.5918, -757.9016, -808.0310])
        m2 = Matrix([-172.0741, -176.5225, 469.0590, 885.3333, 94.6727])

        expected = Matrix(
            [477.0836 + -172.0741, -26.9211 + -176.5225, -23.5918 + 469.0590, -757.9016 + 885.3333, -808.0310 + 94.6727]
        )
        self.assertEqual(m1 + m2, expected)

    def test_add_rows_different_dimension(self):
        m1 = Matrix([939.6196, -592.3947, 440.4948, 10.8480, 450.2958])
        m2 = Matrix([-533.3139, 223.5007, -175.3872])

        with self.assertRaises(ValueError) as context:
            m1 + m2

        self.assertTrue("Matrices do not have the same dimensions." in str(context.exception))

    def test_add_matrices_same_dimension(self):
        m1 = Matrix(
            [88.6714, -875.8507, -237.6208, -250.2987, 840.7898], [-30.5534, 500.8858, -989.3206, 916.9662, -160.3094]
        )
        m2 = Matrix(
            [-782.6808, -508.4920, 364.5909, -312.3470, -551.7485], [-851.3694, -664.6529, 32.0538, 849.8367, -867.5607]
        )

        expected = Matrix(
            [
                88.6714 + -782.6808,
                -875.8507 + -508.4920,
                -237.6208 + 364.5909,
                -250.2987 + -312.3470,
                840.7898 + -551.7485,
            ],
            [
                -30.5534 + -851.3694,
                500.8858 + -664.6529,
                -989.3206 + 32.0538,
                916.9662 + 849.8367,
                -160.3094 + -867.5607,
            ],
        )
        self.assertEqual(m1 + m2, expected)

    def test_add_matrices_different_dimension(self):
        m1 = Matrix(
            [141.8632, -335.6889, 608.2648, 603.2316, 515.6412], [310.9895, 349.2671, 653.2981, -9.2391, -956.2110]
        )
        m2 = Matrix([687.5014, -429.3041, 914.3322, -189.3483, 594.7063])

        with self.assertRaises(ValueError) as context:
            m1 + m2

        self.assertTrue("Matrices do not have the same dimensions." in str(context.exception))

    def test_mul_row_and_column_compatible(self):
        m1 = Matrix([-20.5973, 709.9571, -265.7746, 377.5217, 632.4972])
        m2 = Matrix([-296.9126], [-380.7109], [980.3733], [169.2157], [527.5249])

        expected = Matrix(
            [
                -20.5973 * -296.9126
                + 709.9571 * -380.7109
                + -265.7746 * 980.3733
                + 377.5217 * 169.2157
                + 632.4972 * 527.5249
            ]
        )

        self.assertEqual(m1 * m2, expected)

    def test_mul_row_and_column_incompatible(self):
        m1 = Matrix([101.6459, 407.3730, -26.1866, 984.6866, -82.9196])
        m2 = Matrix([643.9705], [-909.2394])

        with self.assertRaises(ValueError) as context:
            m1 * m2

        self.assertTrue("Matrices have incompatible dimensions." in str(context.exception))

    def test_mul_compatible_matrices(self):
        m1 = Matrix(
            [508.1877, -582.2207, 691.5922, -775.7616, -369.7584], [-567.9043, 690.7085, -669.2538, -932.1922, 698.7102]
        )
        m2 = Matrix(
            [-417.2237, 924.5266],
            [-757.1073, 468.2619],
            [900.1731, -141.9931],
            [142.6938, 271.9839],
            [-176.2502, -430.8799],
        )

        expected = Matrix([805801.9056560401, 47326.75180559003], [-1144607.44190332, -661182.1865100102])

        self.assertEqual(m1 * m2, expected)

    def test_mul_incompatible_matrices(self):
        m1 = Matrix(
            [-406.3560, 628.4193, 777.7030, 59.7072, -773.4369], [981.0062, -520.7840, -947.3464, 62.6381, -681.6100]
        )
        m2 = Matrix([-125.7764, -508.6450, 128.9235, 921.4412, 452.9932])

        with self.assertRaises(ValueError) as context:
            m1 * m2

        self.assertTrue("Matrices have incompatible dimensions." in str(context.exception))

    def test_transpose_column(self):
        m = Matrix([-758.6576], [501.6800], [677.6861], [211.8312], [-450.2701])

        expected = Matrix([-758.6576, 501.6800, 677.6861, 211.8312, -450.2701])

        self.assertEqual(m.transpose(), expected)

    def test_transpose_row(self):
        m = Matrix([193.1112, -994.0469, 460.1026, 475.3871, -842.0641])

        expected = Matrix([193.1112], [-994.0469], [460.1026], [475.3871], [-842.0641])

        self.assertEqual(m.transpose(), expected)

    def test_transpose_matrix(self):
        m = Matrix(
            [-12.7372, -378.3153, -63.2416, -183.4155, 454.4996],
            [717.2233, 209.9556, -414.3130, 594.6258, 324.4141],
            [496.6713, 311.3712, -226.6884, 156.4135, 305.0885],
        )

        expected = Matrix(
            [-12.7372, 717.2233, 496.6713],
            [-378.3153, 209.9556, 311.3712],
            [-63.2416, -414.3130, -226.6884],
            [-183.4155, 594.6258, 156.4135],
            [454.4996, 324.4141, 305.0885],
        )

        self.assertEqual(m.transpose(), expected)

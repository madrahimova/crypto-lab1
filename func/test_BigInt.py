from unittest import TestCase
from func.BigInt import BigInt


class TestSmallBigInt(TestCase):
    def setUp(self) -> None:
        self.a = BigInt(1)
        self.b = BigInt(2)

    def test_add(self):
        c = self.a.add(self.b)
        self.assertEqual(c.equals(BigInt(3)), True)

    def test_mul(self):
        c = self.a.mul(self.b)
        self.assertEqual(c.equals(BigInt(2)), True)

    def test_divide(self):
        c = self.a.divide(2)
        self.assertEqual(c[0].equals(BigInt(0)), True)
        self.assertEqual(c[1].equals(BigInt(1)), True)

    def test_mod(self):
        c = self.a.mod(self.b)
        self.assertEqual(c.equals(BigInt(1)), True)


class TestPosBigInt(TestCase):
    def setUp(self) -> None:
        self.pos_a = BigInt('1245356356356356353635634888')
        self.pos_b = BigInt(1)

    def test_add(self):
        c = self.pos_a.add(self.pos_b)
        self.assertEqual(c.equals(BigInt('1245356356356356353635634889')), True)

    def test_mul(self):
        c = self.pos_a.mul(self.pos_b)
        self.assertEqual(c.equals(BigInt('1245356356356356353635634888')), True)

    def test_divide(self):
        c = self.pos_a.divide(1)
        self.assertEqual(c[0].equals(BigInt('1245356356356356353635634888')), True)
        self.assertEqual(c[1].equals(BigInt(0)), True)

    def test_mod(self):
        c = self.pos_a.mod(self.pos_b)
        self.assertEqual(c.equals(BigInt(0)), True)


class TestNegBigInt(TestCase):
    def setUp(self) -> None:
        self.neg_a = BigInt('-1245356356356356353635634888')
        self.neg_b = BigInt(-1)

    def test_add(self):
        c = self.neg_a.add(self.neg_b)
        self.assertEqual(c.equals(BigInt('-1245356356356356353635634889')), True)

    def test_mul(self):
        c = self.neg_a.mul(self.neg_b)
        self.assertEqual(c.equals(BigInt('1245356356356356353635634888')), True)

    def test_divide(self):
        c = self.neg_a.divide(-1)
        self.assertEqual(c[0].equals(BigInt('1245356356356356353635634888')), True)
        self.assertEqual(c[1].equals(BigInt(0)), True)

    def test_mod(self):
        c = self.neg_a.mod(self.neg_b)
        self.assertEqual(c.equals(BigInt(0)), True)


class TestPosNegBigInt(TestCase):
    def setUp(self) -> None:
        self.pos_a = BigInt('1245356356356356353635634888')
        self.neg_b = BigInt(-1)

    def test_add(self):
        c = self.pos_a.add(self.neg_b)
        self.assertEqual(c.equals(BigInt('1245356356356356353635634887')), True)

    def test_mul(self):
        c = self.pos_a.mul(self.neg_b)
        self.assertEqual(c.equals(BigInt('1245356356356356353635634888')), True)
        self.assertTrue(c.sign)

    def test_divide(self):
        c = self.pos_a.divide(-1)
        self.assertEqual(c[0].equals(BigInt('1245356356356356353635634888')), True)
        self.assertTrue(c[0].sign)
        self.assertEqual(c[1].equals(BigInt(0)), True)

    def test_mod(self):
        c = self.pos_a.mod(self.neg_b)
        self.assertEqual(c.equals(BigInt(0)), True)

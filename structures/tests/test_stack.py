from unittest import TestCase, main

from structures.queues import Stack, EmptyQueueError


class TestStack(TestCase):
    def test_init(self):
        stack = Stack[int]()

        self.assertIsNone(stack.head)
        self.assertEqual(len(stack), 0)

    def test_push_to_empty_stack(self):
        stack = Stack[int]()
        stack.push(5)

        self.assertEqual(stack.head.value, 5)
        self.assertEqual(len(stack), 1)

    def test_pop_from_empty_stack(self):
        stack = Stack[int]()

        with self.assertRaises(EmptyQueueError):
            stack.pop()

    def test_pop_from_stack(self):
        stack = Stack[int]()
        stack.push(5)
        stack.push(7)
        stack.push(9)

        value = stack.pop()

        self.assertEqual(value, 9)
        self.assertEqual(stack.head.value, 7)
        self.assertEqual(len(stack), 2)


if __name__ == '__main__':
    main()

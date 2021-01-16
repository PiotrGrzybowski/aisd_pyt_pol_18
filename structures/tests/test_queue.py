from unittest import TestCase, main

from structures.queues import Queue, EmptyQueueError


class TestQueue(TestCase):
    def test_init(self):
        queue = Queue[int]()

        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)
        self.assertEqual(queue.size, 0)

    def test_push_to_empty_queue(self):
        queue = Queue[int]()
        queue.push(5)

        self.assertEqual(queue.head.value, 5)
        self.assertEqual(queue.tail.value, 5)
        self.assertEqual(len(queue), 1)
        self.assertIsNone(queue.head.next)
        self.assertIsNone(queue.tail.next)

    def test_push_to_one_element_queue(self):
        queue = Queue[int]()
        queue.push(5)
        queue.push(7)

        self.assertEqual(queue.head.value, 5)
        self.assertEqual(queue.tail.value, 7)
        self.assertEqual(len(queue), 2)

        self.assertEqual(queue.head.next.value, 7)
        self.assertIsNone(queue.tail.next)

    def test_push_to_many_element_queue(self):
        queue = Queue[int]()
        queue.push(5)
        queue.push(7)
        queue.push(9)

        self.assertEqual(queue.head.value, 5)
        self.assertEqual(queue.tail.value, 9)
        self.assertEqual(len(queue), 3)

    def test_pop_from_empty_queue(self):
        queue = Queue[int]()

        with self.assertRaises(EmptyQueueError):
            queue.pop()

    def test_pop_from_one_element_queue(self):
        queue = Queue[int]()
        queue.push(5)
        value = queue.pop()

        self.assertEqual(value, 5)
        self.assertEqual(len(queue), 0)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_pop_from_many_element_queue(self):
        queue = Queue[int]()
        queue.push(5)
        queue.push(7)
        value = queue.pop()

        self.assertEqual(value, 5)
        self.assertEqual(len(queue), 1)

        self.assertEqual(queue.head.value, 7)
        self.assertEqual(queue.tail.value, 7)

    def test_read_from_queue(self):
        queue = Queue[int]()
        queue.push(5)
        queue.push(7)
        value = queue.front()

        self.assertEqual(queue.head.value, 5)
        self.assertEqual(len(queue), 2)
        self.assertEqual(value, 5)


if __name__ == '__main__':
    main()

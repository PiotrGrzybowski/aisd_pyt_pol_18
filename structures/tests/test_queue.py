from unittest import TestCase, main
from structures.queues import Queue


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


if __name__ == '__main__':
    main()

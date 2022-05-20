# add ListNode definition to solution.py
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import solution


def stringToList(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    dummy = solution.ListNode(0)
    cur = dummy
    for v in inputValues:
        cur.next = solution.ListNode(v)
        cur = cur.next

    return dummy.next


def listToString(head: solution.ListNode):
    if not head:
        return '[]'
    s = '[' + str(head.val)
    head = head.next
    while head:
        s += ',' + str(head.val)
        head = head.next
    s += ']'
    return s

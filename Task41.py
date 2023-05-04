class Node:
    def __init__(self, coef, power):
        self.coef = coef
        self.power = power
        self.next = None

def create_polynomial():
    head = None
    tail = None

    n = int(input())
    coefs = list(map(int, input().split()))

    for i in range(n+1):
        if coefs[i] != 0:
            node = Node(coefs[i], n-i)
            if not head:
                head = node
            else:
                tail.next = node
            tail = node

    return head


def add_polynomials(p, q):
    head = None
    tail = None

    while p or q:
        if p and q:
            if p.power > q.power:
                coef = p.coef
                power = p.power
                p = p.next
            elif q.power > p.power:
                coef = q.coef
                power = q.power
                q = q.next
            else:
                coef = p.coef + q.coef
                power = p.power
                p = p.next
                q = q.next
        elif p:
            coef = p.coef
            power = p.power
            p = p.next
        else:
            coef = q.coef
            power = q.power
            q = q.next

        node = Node(coef, power)
        if not head:
            head = node
        else:
            tail.next = node
        tail = node

    return head

def print_polynomial(head):
    node = head
    coefs = []

    while node:
        coefs.append(node.coef)
        node = node.next

    print(len(coefs) - 1)
    print(' '.join(map(str, reversed(coefs))))

p = create_polynomial()
q = create_polynomial()

r = add_polynomials(p, q)

print_polynomial(r)
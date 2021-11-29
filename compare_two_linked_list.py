def compare_lists(llist1, llist2):
    # temp = llist1
    # prev = llist2
    # while temp and prev:
    #     if temp.data == prev.data:
    #         temp = temp.next
    #         prev = prev.next
    #     else:
    #         return 0
    # if temp or prev:
    #     return 0
    # return 1
    if not llist1 and not llist2:
        return 1
    if not llist1 or not llist2:
        return 0
    if llist1.data == llist2.data:
        return compare_lists(llist1.next, llist2.next)
    else:
        return 0

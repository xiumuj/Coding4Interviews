### 题目描述

给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

首先要确定是否包含环。（这个题在第二版书中是位于 链表倒数第k个结点 之后的，所以思路上会有些类似。）确定的方法是，两个指针同时从头出发，一个一次走一步，一个一次走两步，当快指针和慢指针重逢了，说明存在环，如果快指针走到了链表末尾，也没有和慢的重逢过，说明不包含环。

第二步是找出环的入口。仍然可以用两个指针，如图的环有4个节点，那么让p1先走4步，然后p1 p2 一起走，当两个指针重逢时，由于两个指针差距应该是环的长度，而他俩重逢了，说明p1已经绕环走了一圈，重逢的位置就是环的入口。说明重逢点右边即是环的长度

如何找到环的长度？在前面判断是否有环时，如果快慢指针相遇则说明有环，此时相遇的节点必定在环中，记住这个节点然后从它出发，等再次回到这个节点时就走了一圈，就得到环的长度了。

所以这个题的关键在于，要知道如何判断是否包含环、如何计算环长度、如何通过两个指针差距的方法找到环的入口。

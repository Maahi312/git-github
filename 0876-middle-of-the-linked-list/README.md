<h2><a href="https://leetcode.com/problems/middle-of-the-linked-list">876. Middle of the Linked List</a></h2><h3>Easy</h3><hr><p>Given the <code>head</code> of a singly linked list, return <em>the middle node of the linked list</em>.</p>

<p>If there are two middle nodes, return <strong>the second middle</strong> node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg" style="width: 544px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [3,4,5]
<strong>Explanation:</strong> The middle node of the list is node 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg" style="width: 664px; height: 65px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5,6]
<strong>Output:</strong> [4,5,6]
<strong>Explanation:</strong> Since the list has two middle nodes with values 3 and 4, we return the second one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>


---
# Approach

I am using the Two Pointers (Slow & Fast) technique here:

1. node1 → slow pointer → moves 1 step at a time

2. node2 → fast pointer → moves 2 steps at a time


---
At a particular not the node1 is decided as the middle node. Why it works as a middle node, because

1. Since node2 moves twice as fast as node1, by the time node2 reaches the end of the list,
node1 has covered half the distance — i.e., it’s at the middle.

2. The loop stops when node2 or node2.next becomes None, ensuring we don’t go beyond the list’s end

---

# 💡 In Summary

1. node1 → moves one step (slow)

2. node2 → moves two steps (fast)

3. When node2 reaches end → node1 is in the middle

4. Works for both odd and even length lists

---

# Time & Space Complexity : single pass (O(n)) and constant space (O(1))

<h2><a href="https://leetcode.com/problems/ransom-note">383. Ransom Note</a></h2><h3>Easy</h3><hr><p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
</ul>


---

# Step 1 — Create a frequency dictionary

Initialize an empty dictionary called letter.

Loop through each character in magazine.

For every letter:

If it already exists in the dictionary → increment its count.

If it doesn’t exist → add it to the dictionary with a count of 1.

This gives us a count of available letters from the magazine.

---

# Step 2 — Check each letter in ransomNote

Loop through every character in ransomNote.

For each letter:

If it’s not in letter (not available) → return False.

If the count for that letter is 0 (used up) → return False.

Otherwise, use one → decrement the count by 1.

---

# Step 3 — Return True if all letters matched

If the loop finishes (no missing or overused letters found), return True.

That means every letter in ransomNote was successfully found and used from the magazine.

---

<h2><a href="https://leetcode.com/problems/zigzag-conversion">6. Zigzag Conversion</a></h2><h3>Medium</h3><hr><p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 4
<strong>Output:</strong> &quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A&quot;, numRows = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>&#39;,&#39;</code> and <code>&#39;.&#39;</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>

---

# Step by Step Explanation

<h3>Function signature:</h3>

def convert(self, s: str, numRows: int) -> str:


s → input string you want to convert.

numRows → number of rows in the zigzag pattern.

-> str → the function will return a string.

# Edge case check:

if numRows == 1 or numRows >= len(s):
    return s


If there’s only 1 row, there’s no zigzag, so return s.

If the number of rows is greater than or equal to the string length, zigzag is same as original string.

# Initialize rows:

row = [''] * numRows


row is a list of strings, not a string itself.

Each element will store characters for that row.

Example: if numRows = 3, row looks like ['', '', ''] at the start.

# Current row pointer & direction:

curr = 0
nex = False


curr → tells which row we are currently adding a character to.

nex → a boolean that tells direction:

True → moving down

False → moving up

# Traverse each character:

for char in s:
    row[curr] += char


Add the character char to the current row (row[curr]).

Example: if curr = 0 and char = 'P', then row[0] = 'P'.

# Change direction at top/bottom:

if curr == 0 or curr == numRows - 1:
    nex = not nex


If we reach top row (0) or bottom row (numRows - 1), reverse direction.

This is what creates the zigzag movement.

# Move pointer:

curr += 1 if nex else -1


If nex = True (moving down) → curr += 1

If nex = False (moving up) → curr -= 1

# Combine rows into final string:

return ''.join(row)


row is a list of strings, e.g., ['PAHN', 'APLSIIG', 'YIR'].

''.join(row) → merges all rows into a single string.

Returns the final zigzag string.

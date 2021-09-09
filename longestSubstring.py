def longestSubstring(s):
  window = set()
  r = 0
  l = 0
  longest = 0
  while r < len(s):
    if s[r] not in window:
      window.add(s[r])
      r += 1
    else:
      window.remove(s[l])
      l += 1
    longest = max(longest, r-l)
  return longest
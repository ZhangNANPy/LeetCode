# -*- coding: utf-8 -*-
# @File  : 68_TextJustification.py
# @Author: ZRN
# @Date  : 2019/5/6
"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        rows = []
        r = -1
        left_space = maxWidth
        i = 0
        while i < len(words):
            if left_space == maxWidth:
                rows.append([])
                r += 1
            if left_space >= len(words[i]):
                rows[r].append(words[i])
                left_space -= (len(words[i]) + 1)
                i += 1
            else:
                rows[r].append(left_space + 1)
                left_space = maxWidth
        lls = maxWidth - len(rows[-1]) + 1 - sum([len(w) for w in rows[-1]])
        last = ' '.join(rows[-1]) + ' ' * lls
        del rows[-1]
        res = []
        for row in rows:
            if len(row) == 2:
                res.append(row[0] + ' ' * row[1])
            else:
                bs = row[-1] // (len(row) - 2)
                es = row[-1] - bs * (len(row) - 2)
                t = ''
                for i in range(len(row) - 2):
                    t += row[i] + ' ' * (bs + 1)
                    if es:
                        t += ' '
                        es -= 1
                t += row[-2]
                res.append(t)
        res.append(last)
        return res


if __name__ == '__main__':
    s = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(s.fullJustify(words, 16))

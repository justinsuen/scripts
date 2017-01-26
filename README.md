# Scripts

Here are some scripts I wrote for myself:
- [`word_doc_stats.py`](word_doc_stats.py) reads a text file and displays the word count, char count and the most frequent words based on minimum length and minimum frequency desired.
- [`dsv_to_json.rb`](dsv_to_json.rb) parses a "delimiter separated values" file by the specified delimiter and returns an array of lines with corresponding values. It also has a method to parse this array into a JSON-friendly object. A notable use of this is found in the [`seed.rb`](https://github.com/justinsuen/chartesian/blob/master/db/seeds.rb) file of my personal project [Chartesian](http://www.chartesian.com).

Utility for converting Magic: the Gathering deck lists into the format used by Forge.

For example:
Input | Output
-------- | --------
Deck | Main
1 Charming Prince (ELD) 8 | 1 Charming Prince|ELD|
8 Plains (IKO) 262 | 8 Plains|IKO|

***


Task list:
- [x] Basic functionality
- [ ] Handle newlines between sections
- [ ] Better handling for section titles
- [ ] Optionally load deck list from file
- [ ] Support additional formats
- [ ] Polished CLI
- [ ] Optionally print deck stats (mana curve graph, avg. mana cost, colors, etc)
- [ ] Optimize performance.
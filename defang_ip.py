# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(self, address: str) -> str:
        store = defaultdict(list)
        address = list(address)
        print('length', len(address))
        i = 1
        dots = address.count('.')
        limit = len(address)+dots
        while i <= limit:
            if (address[i] == '.'):
                address.insert(i,'[')
                address.insert(i+2,']')
                i += 1
            i += 1
        return ''.join(address)
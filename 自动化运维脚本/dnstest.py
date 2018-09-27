#!/usr/bin/env python
import dns.resolver
domian = raw_input('please input an domain:')
A = dns.resolver.query(domian, 'A')
for i   in  A.response.answer:
    for j   in  i.items:
        print j
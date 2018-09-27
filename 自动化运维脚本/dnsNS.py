#!/usr/bin/env python
import dns.resolver
domian = raw_input('please input an domain:')
ns = dns.resolver.query(domian, 'NS')
for i   in  ns.response.answer:
    for j   in  i.items:
        print j.to_text()
import dns.resolver

while True:
    domains = ['httpbin.org', 'google.com', 'yahoo.com']
    record_types = ['A', 'MX', 'TXT']

    for domain in domains:
        print(f"Consultando registros para el dominio {domain}:")
        for record_type in record_types:
            try:
                answers = dns.resolver.query(domain, record_type)
                for rdata in answers:
                    print(rdata)
            except dns.resolver.NoAnswer:
                print(f"No se encontraron registros de tipo {record_type} para el dominio {domain}")
            except dns.resolver.NXDOMAIN:
                print(f"No se encontró el dominio {domain}")
            except dns.exception.Timeout:
                print("La consulta ha expirado, intente nuevamente más tarde.")
from pathlib import Path
from boleto_cloud.boletos import Boleto


if __name__ == "__main__":
    boleto_token = "ACin7NWnpRVC-dpjKqu4b5LVR7T1vcbE9UmhAm-Qa9g"
    BC = Boleto()
    boleto_data = {
        "boleto.conta.banco": "237",
        "boleto.conta.agencia": "1234-5",
        "boleto.conta.numero": "123456-0",
        "boleto.conta.carteira": "12",
        "boleto.beneficiario.nome": "DevAware Solutions",
        "boleto.beneficiario.cprf": "15.719.277/0001-46",
        "boleto.beneficiario.endereco.cep": "59020-000",
        "boleto.beneficiario.endereco.uf": "RN",
        "boleto.beneficiario.endereco.localidade": "Natal",
        "boleto.beneficiario.endereco.bairro": "Petrópolis",
        "boleto.beneficiario.endereco.logradouro": "Avenida Hermes da Fonseca",
        "boleto.beneficiario.endereco.numero": "384",
        "boleto.beneficiario.endereco.complemento": "Sala 2A, segundo andar",
        "boleto.emissao": "2014-07-11",
        "boleto.vencimento": "2020-05-30",
        "boleto.documento": "EX1",
        "boleto.numero": "12345678901-P",
        "boleto.titulo": "DM",
        "boleto.valor": "1250.43",
        "boleto.pagador.nome": "Alberto Santos Dumont",
        "boleto.pagador.cprf": "111.111.111-11",
        "boleto.pagador.endereco.cep": "36240-000",
        "boleto.pagador.endereco.uf": "MG",
        "boleto.pagador.endereco.localidade": "Santos Dumont",
        "boleto.pagador.endereco.bairro": "Casa Natal",
        "boleto.pagador.endereco.logradouro": "BR-499",
        "boleto.pagador.endereco.numero": "s/n",
        "boleto.pagador.endereco.complemento": "Sï¿½tio - Subindo a serra da Mantiqueira",
        "boleto.instrucao": "Atenção! NÃO RECEBER ESTE BOLETO.",
        "boleto.instrucao": "Este é apenas um teste utilizando a API Boleto Cloud",
        "boleto.instrucao": "Mais info em http://www.boletocloud.com/app/dev/api"
    }

    r = BC.create(data=boleto_data)
    print(r.status_code)
    if r.status_code == 200:
        Path("boleto-gerado-teste.pdf").write_bytes(r.content)
    else:
        print(r.content)

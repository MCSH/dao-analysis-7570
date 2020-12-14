# -*- coding: utf-8 -*-
"""

@author: Monika Sharma
"""
import requests
import json


contract_addresses=["0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2"
,"0x448a5065aebb8e423f0896e6c5d525c040f59af3"
,"0xbda109309f9fafa6dd6a9cb9f1df4085b27ee8ef"
,"0x9b0f70df76165442ca6092939132bbaea77f2d7a"
,"0x9b0ccf7c8994e19f39b2b4cf708e0a7df65fa8a3"
,"0xf2c5369cffb8ea6284452b0326e326dbfdcb867c"
,"0x315cbb88168396d12e1a255f9cb935408fe80710"
,"0x79f6d0f646706e1261acf0b93dcb864f357d4680"
,"0x8e2a84d6ade1e7fffee039a35ef5f19f13057152"
,"0x69076e44a9c70a67d5b79d95795aba299083c275"
,"0xa26e15c895efc0616177b7c1e7270a4c7d51c997"
,"0x36a724bd100c39f0ea4d3a20f7097ee01a8ff573"
,"0x9ef05f7f6deb616fd37ac3c959a2ddd25a54e4f5"
,"0x78f2c2af65126834c51822f56be0d7469d7a523e"
,"0xbaa65281c2fa2baacb2cb550ba051525a480d3f4"
,"0xab14d3ce3f733cacb76ec2abe7d2fcb00c99f3d5"
,"0x0581a0abe32aae9b5f0f68defab77c6759100085"
,"0xdfe0fb1be2a52cdbf8fb962d5701d7fd0902db9f"
,"0xaa745404d55f88c108a28c86abe7b5a1e7817c07"
,"0xd8a04f5412223f513dc55f839574430f5ec15531"
,"0x5432b2f3c0dff95aa191c45e5cbd539e2820ae72"
,"0xbe00fe8dfd9c079f1e5f5ad7ae9a3ad2c571fcac"
,"0x4f5f0933158569c026d617337614d00ee6589b6e"
,"0x3d0b1912b66114d4096f48a8cee3a56c231772ca"
,"0x9759a6ac90977b93b58547b4a71c78317f391a28"
,"0x2f0b23f53734252bda2277357e97e1517d6b042a"
,"0xad37fd42185ba63009177058208dd1be4b136e6b"
,"0x19c0976f590d67707e62397c87829d896dc0f1f1"
,"0xbe286431454714f511008713973d3b053a2d38f3"
,"0xbe8e3e3618f7474f8cb1d074a26affef007e98fb"
,"0x197e90f9fad81970ba7976f33cbd77088e5d7cf7"
,"0x65c79fcb50ca1594b025960e539ed7a9a6d434a3"
,"0x35d1b3f3d7966a1dfe207aa4514c12a259a0492b"
,"0xa950524441892a31ebddf91d3ceefa04bf454466"
,"0x99041f808d598b782d5a3e498681c2452a31da08"
,"0x729d19f657bd0614b4985cf1d82531c67569197b"
,"0xc73e0383f3aff3215e6f04b0331d58cecf0ab849"
,"0xe4b22d484958e582098a98229a24e8a43801b674"
,"0x5e227ad1969ea493b43f840cff78d08a6fc17796"
,"0x8ee7d9235e01e6b42345120b5d270bdb763624c7"
,"0x793ebbe21607e4f04788f89c7a9b97320773ec59"
,"0xc66ea802717bfb9833400264dd12c2bceaa34a6d"
,"0xb4eb54af9cc7882df0121d26c5b97e802915abe6"
,"0x81fe72b5a8d1a857d176c3e7d5bd2679a9b85763"
,"0x54003dbf6ae6cba6ddae571ccdc34d834b44ab1e"
,"0x82ecd135dce65fbc6dbdd0e4237e0af93ffd5038"
,"0x07ee93aeea0a36fff2a9b95dd22bd6049ee54f26"
,"0x069b2fb501b6f16d1f5fe245b16f6993808f1008"
,"0x1b93556ab8dccef01cd7823c617a6d340f53fb58"
,"0x6bda13d43b7edd6cafe1f70fb98b5d40f61a1370"
,"0x4678f0a6958e4d2bc4f1baf7bc52e8f3564f3fe4"
,"0x190c2cfc69e68a8e8d5e2b9e2b9cc3332caff77b"
,"0x526af336d614ade5cc252a407062b8861af998f5"
,"0xbf72da2bd84c5170618fbe5914b0eca9638d5eb5"
,"0x794e6e91555438afc3ccf1c5076a74f42133d08d"
,"0x14fbca95be7e99c15cc2996c6c9d841e54b79425"
,"0xb7ac09c2c0217b07d7c103029b4918a2c401eecb"
,"0xf53ad2c6851052a81b42133467480961b2321c09"
,"0x59adcf176ed2f6788a41b8ea4c4904518e62b6a4"
,"0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359"];

#Directory to save files
dir_name="F:\\UofM\\Blockchain Data Analytics\\Project\\ContractTransactions\\";

#Generate API UR 
api_address_prefix='https://api.etherscan.io/api?module=account&action=txlist&address=';
api_address_suffix='&startblock=0&endblock=99999999&sort=asc&apikey=ITA3BQYE6YTTUBA3SXUME2ZETSW6QGRX6S';

count=0;
#Loop for all addresses
for address in contract_addresses:
    api_addr=str(api_address_prefix)+address+str(api_address_suffix);
    resp = requests.get(str(api_addr));
    j_resp = json.loads(resp.text);

    #File name as contract address
    file_name= str(address)+".json"; 
    
    #Save output in file
    with open(str(dir_name)+str(file_name), "a") as outfile:
        json.dump(j_resp["result"], outfile)
        outfile.close();
    count=count+1;
    print(str(count) + " Done")
 
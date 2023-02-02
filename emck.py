import requests
import re

def emck(EMAIL):
    WSP = r'[ \t]'                                       
    CRLF = r'(?:\r\n)'                                   
    NO_WS_CTL = r'\x01-\x08\x0b\x0c\x0f-\x1f\x7f'        
    QUOTED_PAIR = r'(?:\\.)'                             
    FWS = r'(?:(?:' + WSP + r'*' + CRLF + r')?' + WSP + r'+)'                                    
    CTEXT = r'[' + NO_WS_CTL + r'\x21-\x27\x2a-\x5b\x5d-\x7e]'              
    CCONTENT = r'(?:' + CTEXT + r'|' + QUOTED_PAIR + r')'                                                                         
    COMMENT = r'\((?:' + FWS + r'?' + CCONTENT + r')*' + FWS + r'?\)'                       
    CFWS = r'(?:' + FWS + r'?' + COMMENT + ')*(?:' + FWS + '?' + COMMENT + '|' + FWS + ')'         
    ATEXT = r'[\w!#$%&\'\*\+\-/=\?\^`\{\|\}~]'           
    ATOM = CFWS + r'?' + ATEXT + r'+' + CFWS + r'?'      
    DOT_ATOM_TEXT = ATEXT + r'+(?:\.' + ATEXT + r'+)*'   
    DOT_ATOM = CFWS + r'?' + DOT_ATOM_TEXT + CFWS + r'?' 
    QTEXT = r'[' + NO_WS_CTL + r'\x21\x23-\x5b\x5d-\x7e]'                   
    QCONTENT = r'(?:' + QTEXT + r'|' + QUOTED_PAIR + r')'                        
    QUOTED_STRING = CFWS + r'?' + r'"(?:' + FWS + r'?' + QCONTENT + r')*' + FWS + r'?' + r'"' + CFWS + r'?'
    LOCAL_PART = r'(?:' + DOT_ATOM + r'|' + QUOTED_STRING + r')'                    
    DTEXT = r'[' + NO_WS_CTL + r'\x21-\x5a\x5e-\x7e]'    
    DCONTENT = r'(?:' + DTEXT + r'|' + QUOTED_PAIR + r')'                        
    DOMAIN_LITERAL = CFWS + r'?' + r'\[' + r'(?:' + FWS + r'?' + DCONTENT + r')*' + FWS + r'?\]' + CFWS + r'?'  
    DOMAIN = r'(?:' + DOT_ATOM + r'|' + DOMAIN_LITERAL + r')'                       
    ADDR_SPEC = LOCAL_PART + r'@' + DOMAIN               

    VALID_ADDRESS_REGEXP = re.compile(r'^' + ADDR_SPEC + r'$')
    if re.match(VALID_ADDRESS_REGEXP, EMAIL) is not None:
        url = "https://api.mailcheck.ai/{}/{}"
        if '@' in EMAIL:
            response = requests.request("GET", url.format('email',EMAIL))    
        else:
            response = requests.request("GET", url.format('domain',EMAIL))
        return response.text
    else:
        return "Email format is not valid"

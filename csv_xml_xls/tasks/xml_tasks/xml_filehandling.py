'''
Get xml file from attachments and get following details from it.
Read tag between specific tag.
Read value of specific tag using tag's attribute.
'''
import xml.etree.ElementTree as et

def temp_check():
    '''
    :func:
    It will check 'movie.xml' file and parse it, 
    it will write data using write() method for permanently
    User can check it final added data in xml file  
    '''
    temp_tree = et.parse('movie.xml')
    temp_root = temp_tree.getroot()
    
    '''Save new data Permanently in file'''
    temp_root.attrib['title']='Now you see me'
    print(temp_root.attrib)
    temp_tree.write('movie.xml')
    
    '''Can check it data would saved or not'''
    for movie_list in temp_root.iter('movie'):
        print(movie_list.attrib)

''' Call temp_check'''
# temp_check()

'''
Read tags between tags
Read value of that specific attribute
'''
tree = et.parse('account.xml')
root = tree.getroot()
for child_tag in root.iter('template'):
    for key,value in child_tag.items():
        if value == '_assets_backend_helpers':            
            for child_tag1 in child_tag:
                for child_tag2 in child_tag1.iter('link'):
                    print(child_tag.tag,'\n\t',child_tag1.tag,'\n\t\t',child_tag2.tag,child_tag2.attrib)


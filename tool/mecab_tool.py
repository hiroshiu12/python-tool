def create_voclist(sentence,in_pos=['名詞','感動詞'],stop_word = [],inc_num=False):
    """
    sentence : string, assume natural sentence to be analyze
    in_pos : part of speech to be excluded
    output : list which consists of tokens which compose sentence.
    """
    # output format is standard format of MeCab
    tagger = MeCab.Tagger('-b 100000')
    # container to store vocabraly
    voc_list = []
    # container of vocabraly
    morpho = tagger.parse(sentence)
    morpho_list = morpho.split('\n')
    # regular expression to eliminate number
    reg_ex = re.compile(r'\d+')
    
    for row in morpho_list:
        voc = row.split('\t')[0]
        # End of list
        if voc == 'EOS':
            break
        # part of speech
        pos = row.split('\t')[1].split(',')[0]
            
        # eliminate number
        if inc_num and (row.split('\t')[1].split(',')[1] == '数' or reg_ex.match(voc)):
            continue
        
        # Check part of speech
        if pos not in in_pos:
            continue
        # add to voc_list    
        voc_list.append(voc)
    
    return voc_list

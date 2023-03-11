def create_header():
    """
    Log header
    """
    def line(length=100):
        return '_' * length
    
    def create_guide():
        guide = ''
        guide += '....<depth>....'
        guide += '[<WHERE_IT_COMES_FROM>]'
        guide += ' ' + '->' + ' '
        guide += '<PROMPT>'
        guide += ':' + ' '
        guide += '<details>'
        return guide
    
    def guide_explanations():
        explanations = []
        def add(name, info):
            explanations.append([name, info])
        name = 'depth'
        info = 'indentation shows child-parent relationship'
        add(name, info)
        name = 'WHERE_IT_COMES_FROM'
        info = 'the class that has produced the prompt'
        add(name, info)
        name = 'PROMPT'
        info = 'the event that happened'
        add(name, info)
        name = 'details'
        info = 'the extra details of the event'
        add(name, info)
        return explanations
    
    def create_guide_explanations(guide_explanations):
        txt = ''
        for explanation in guide_explanations:
            txt += '\t' * 2
            txt += '-' + ' '
            txt += explanation[0] # name
            txt += ':' + ' '
            txt += explanation[1] # info
            txt += '\n'
        return txt
    
    def create_top():
        top = ''
        top += 'PIPERABM LOG FILE'
        return top

    txt = ''
    txt += line()
    txt += '\n' * 3
    txt += '\t' + '>>>' + ' ' + create_top()
    txt += '\n' * 2
    txt += '\t' + '-' + ' ' + 'Guide' + ':' + '\n'
    txt += '\t' + create_guide() + '\n'
    explanations = guide_explanations()
    txt += create_guide_explanations(explanations)
    txt += '\n'
    txt += line()
    txt += '\n' * 2
    return txt


if __name__ == "__main__":
    txt = create_header()
    print(txt)
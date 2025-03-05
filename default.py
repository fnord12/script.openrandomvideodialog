import xbmc
import xbmcaddon
import sys
import xbmcgui
import json

def debug(msg, *args):
    try: 
        xbmc.log("OPENRANDOMVIDWIN: " + (str(msg)))
     
        for arg in args:
            print(str(arg))
    except:
        print ("OPENRANDOMVIDWIN: Error in Debugoutput")
        print (msg)
        print (args)
                  
def getListItem(path):
    li = xbmcgui.ListItem("To Search")
    li.setPath(path)
    li.setInfo('video', {})
    displayVideoInfo(li)
    
def displayVideoInfo(li):
    xbmc.executebuiltin('ActivateWindow(12003)')
    dialog = xbmcgui.Dialog()
    dialog.info(li)
    
if (__name__ == '__main__'):
    path = sys.argv[1]
    
    debug('path', path)
    if not path == '':
        getListItem(path)

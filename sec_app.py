# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 07:20:44 2021

@author: fredd
"""

from hydralit import HydraApp
import streamlit as st
import appsas

#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='', layout='wide', initial_sidebar_state='collapsed')

if __name__ == '__main__':

    over_theme = {'txc_inactive': '#FFFFFF'}
    #this is the host application, we add children to it and that's it!
    app = HydraApp(
        title='',
        hide_streamlit_markers=True,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_banner_images=[None,{'header':""},None], 
        banner_spacing=[1,1,1],
        use_navbar=True, 
        navbar_sticky=True,
        navbar_animation=False,
        navbar_theme=over_theme,
        
    )

 #Home button will be in the middle of the nav list now
    app.add_app("PERFIL EDADES", app=appsas.CheatApp(title="PERFIL EDADES"))
    app.add_app("Secure", app=appsas.Secure(title="Secure"))
    app.add_app("Start", app=appsas.StartApp(title='Start'))

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    app.enable_guest_access()

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
    if user_access_level > 1:
        complex_nav = {
            'PERFIL EDADES': ['PERFIL EDADES'],
            'Secure': ['Secure'],
            'Start': ['Start']
            
        }
    elif user_access_level == 1:
        complex_nav = {
            'PERFIL EDADES': ['PERFIL EDADES'],
            'Secure': ['Secure'],
            'Start': ['Start']            
            }
    else:
        complex_nav = {
            'Start': ['Start'],
        }

  
    #and finally just the entire app and all the children.
    app.run(complex_nav)
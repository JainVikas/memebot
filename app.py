# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:11:41 2017

@author: vikas
"""
from flask import Flask, request, jsonify
import os
from pymeme import *

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
meme = MemeGen()
meme.retrieve_api()

templateURL= meme.get_link_templates()
templateDict = meme.get_templates()


exampleUrlList=['https://memegen.link/tenguy/your_text/goes_here.jpg', "https://memegen.link/afraid/i_don't_know_what_this_meme_is_for/and_at_this_point_i'm_too_afraid_to_ask.jpg", "https://memegen.link/older/it's_an_older_meme_sir/but_it_checks_out.jpg", 'https://memegen.link/aag/_/aliens.jpg', 'https://memegen.link/tried/at_least/you_tried.jpg', 'https://memegen.link/biw/gets_iced_coffee/in_the_winter.jpg', "https://memegen.link/stew/_/baby,_you've_got_a_stew_going!.jpg", 'https://memegen.link/blb/your_text/goes_here.jpg', "https://memegen.link/kermit/_/but_that's_none_of_my_business.jpg", "https://memegen.link/bd/can't_workout/don't_want_to_get_too_buff.jpg", 'https://memegen.link/ch/if_you_wanted_to_avoid_the_friend_zone/you_should_have_made_your_intentions_known_from_the_start.jpg', 'https://memegen.link/cbg/_/worst_thing_ever!.jpg', 'https://memegen.link/wonka/your_text/goes_here.jpg', 'https://memegen.link/cb/i_stole/the_pic_i_nic_basket.jpg', 'https://memegen.link/keanu/your_text/goes_here.jpg', 'https://memegen.link/dsm/they_will_never_find_your_body/as_attractive_as_i_do.jpg', 'https://memegen.link/live/_/do_it_live!.jpg', "https://memegen.link/ants/do_you_want_ants~q/because_that's_how_you_get_ants.jpg", 'https://memegen.link/doge/such_meme/very_skill.jpg', 'https://memegen.link/drake/your_text/goes_here.jpg', 'https://memegen.link/ermg/ermahgerd/memes.jpg', 'https://memegen.link/facepalm/your_text/goes_here.jpg', 'https://memegen.link/firsttry/_/first_try!.jpg', 'https://memegen.link/fwp/your_text/goes_here.jpg', 'https://memegen.link/fa/forever/alone.jpg', 'https://memegen.link/fbf/paper_towel/the_plate_that_cleans_up_after_itself.jpg', 'https://memegen.link/fmr/_/fuck_me,_right~q.jpg', 'https://memegen.link/fry/not_sure_if_trolling/or_just_stupid.jpg', 'https://memegen.link/ggg/your_text/goes_here.jpg', 'https://memegen.link/hipster/your_text/goes_here.jpg', 'https://memegen.link/icanhas/i_can_has/this_meme~q.jpg', "https://memegen.link/crazypills/_/i_feel_like_i'm_taking_crazy_pills.jpg", "https://memegen.link/mw/you're_gonna_like_the_way_you_look/i_guarantee_it.jpg", "https://memegen.link/noidea/i_have_no_idea/what_i'm_doing.jpg", 'https://memegen.link/regret/_/i_immediately_regret_this_decision.jpg', 'https://memegen.link/boat/_/i_should_buy_a_boat.jpg', 'https://memegen.link/hagrid/_/i_should_not_have_said_that.jpg', 'https://memegen.link/sohappy/if_i_could_use_this_meme/i_would_be_so_happy.jpg', 'https://memegen.link/captain/look_at_me/i_am_the_captain_now.jpg', "https://memegen.link/bender/i'm_going_to_build_my_own_theme_park/with_blackjack_and_hookers.jpg", 'https://memegen.link/inigo/you_keep_using_that_word/i_do_not_think_it_means_what_you_think_it_means.jpg', 'https://memegen.link/iw/does_testing/in_production.jpg', "https://memegen.link/ackbar/_/it's_a_trap!.jpg", "https://memegen.link/happening/_/it's_happening.jpg", "https://memegen.link/joker/it's_simple/kill_the_batman.jpg", "https://memegen.link/ive/we_think/you'll_love_it.jpg", 'https://memegen.link/ll/_/hhhehehe.jpg', 'https://memegen.link/away/life.../finds_a_way.jpg', 'https://memegen.link/morpheus/your_text/goes_here.jpg', "https://memegen.link/mb/'member/star_wars~q.jpg", 'https://memegen.link/badchoice/milk/was_a_bad_choice.jpg', 'https://memegen.link/mmm/your_text/goes_here.jpg', 'https://memegen.link/jetpack/nothing_to_do_here.jpg', "https://memegen.link/imsorry/oh,_i'm_sorry/i_thought_this_was_america.jpg", "https://memegen.link/red/oh,_is_that_what_we're_going_to_do_today~q/we're_going_to_fight~q.jpg", 'https://memegen.link/mordor/one_does_not_simply/walk_into_mordor.jpg', 'https://memegen.link/oprah/you_get_a_meme/and_you_get_a_meme.jpg', 'https://memegen.link/oag/i_know_you_received_my_email/because_i_checked_your_inbox.jpg', 'https://memegen.link/remembers/remember_this_meme~q/pepperidge_farm_remembers.jpg', 'https://memegen.link/philosoraptor/your_text/goes_here.jpg', 'https://memegen.link/jw/you_just_went_and_made_a_new_dinosaur~q/probably_not_a_good_idea.jpg', 'https://memegen.link/patrick/why_dont_we_take_all_the_memes/and_put_them_on_memegen.jpg', "https://memegen.link/rollsafe/can't_get_fired/if_you_don't_have_a_job.jpg", "https://memegen.link/sad-obama/sad_barack_obama/doesn't_think_you'll_vote.jpg", "https://memegen.link/sad-clinton/sad_bill_clinton/doesn't_think_you'll_vote.jpg", 'https://memegen.link/sadfrog/_/feels_bad_man.jpg', "https://memegen.link/sad-bush/sad_george_bush/doesn't_think_you'll_vote.jpg", "https://memegen.link/sad-biden/sad_joe_biden/doesn't_think_you'll_vote.jpg", "https://memegen.link/sad-boehner/sad_john_boehner/doesn't_think_you'll_vote.jpg", 'https://memegen.link/saltbae/your_text/goes_here.jpg', "https://memegen.link/sarcasticbear/i'm_so_sorry/i_haven't_memorized_the_internet.jpg", 'https://memegen.link/dwight/love_is_all_you_need~q/false._you_need_water_and_rations..jpg', 'https://memegen.link/sb/remembers_the_face/but_not_the_name.jpg', 'https://memegen.link/ss/needs_a_place_to_crash/never_leaves.jpg', 'https://memegen.link/sf/i_accidentally_used_a_swear_word/and_i_know_my_mom_heard_it_from_the_other_room.jpg', 'https://memegen.link/money/shut_up_and/take_my_money!.jpg', 'https://memegen.link/snek/when_you_already_checked_that_one_leaf/and_it_starts_moving.jpg', 'https://memegen.link/sk/you_finished_your_plate/because_i_was_starving~q.jpg', 'https://memegen.link/sohot/this_meme_is/so_hot_right_now.jpg', "https://memegen.link/nice/_/so_i_got_that_goin'_for_me,_which_is_nice.jpg", 'https://memegen.link/awesome-awkward/first_day_at_new_job/spill_coffee_on_bossman.jpg', 'https://memegen.link/awesome/say_a_word_wrong/create_hilarious_inside_joke.jpg', 'https://memegen.link/awkward-awesome/trip_guy_on_the_street/he_was_running_with_a_stolen_purse.jpg', 'https://memegen.link/awkward/start_telling_joke/forget_punchline.jpg', "https://memegen.link/fetch/stop_trying_to_make_fetch_happen/it's_not_going_to_happen.jpg", "https://memegen.link/success/don't_know_a_question_on_the_test/answer_is_in_another_question.jpg", 'https://memegen.link/scc/your_text/goes_here.jpg', "https://memegen.link/ski/_/you're_gonna_have_a_bad_time.jpg", "https://memegen.link/officespace/yeah.../that'd_be_great.jpg", 'https://memegen.link/interesting/your_text/goes_here.jpg', 'https://memegen.link/toohigh/the_rent_is/too_damn_high.jpg', 'https://memegen.link/bs/what_a_surprise.../you_caught_me_again.jpg', 'https://memegen.link/fine/_/this_is_fine.jpg', 'https://memegen.link/sparta/this._is./sparta!.jpg', 'https://memegen.link/whatyear/_/what_year_is_it~q.jpg', 'https://memegen.link/center/what_is_this/a_center_for_ants.jpg', 'https://memegen.link/both/_/why_not_both~q.jpg', 'https://memegen.link/winter/prepare_yourself/winter_is_coming.jpg', 'https://memegen.link/xy/all_the_things!!!.jpg', 'https://memegen.link/buzz/memes/memes_everywhere.jpg', 'https://memegen.link/yodawg/yo_dawg/i_heard_you_like_memes.jpg', 'https://memegen.link/yuno/y_u_no/use_this_meme!~q.jpg', "https://memegen.link/yallgot/y'all_got_any_more_of_them/memes.jpg", 'https://memegen.link/bad/your_meme_is_bad/and_you_should_feel_bad.jpg', 'https://memegen.link/elf/_/you_sit_on_a_throne_of_lies.jpg', 'https://memegen.link/chosen/you_were_the_chosen_one!.jpg']
'''
Remove extra code which delays the server start
aliaseList=[]
for key in templateDict:
    template = meme.get_template(key)
    print(template.get_name())
    aliase=template.get_aliases()[1]
    try:
        example = template.get_example(aliase)
        print(example.get_direct_visible())
        exampleUrlList.append(example.get_direct_visible())
    except:
        pass
   
print(exampleUrlList) 
len(exampleUrlList)

'''

def replaceUnderscores(stringInput):
    return stringInput.replace('_'," ")

def splitLink(exampleUrl):
    t= exampleUrl.split(sep='/')
    if len(t)>=6:
        link= t[0]+ '//'+ t[2] +'/'+t[3]+'/'
        upperText= replaceUnderscores(t[4])
        lowerText= replaceUnderscores(t[5].split('.')[0])
    else:
        link= t[0]+ '//'+ t[2] +'/'+t[3]
        upperText= replaceUnderscores(t[4].split('.')[0])
        lowerText=replaceUnderscores('_')
    return link,upperText,lowerText


@app.route('/images', methods=['POST', 'GET'])
def images():
    inputRecords = request.args.get('inputRecords')

    galleryResponse= {
     "messages": [
    {
      "attachment":{
    "type":"template",
    "payload":{
      "template_type":"generic",
      "image_aspect_ratio": "square",
      "elements":[ ]
    }
      }
    }
      ]
    }

    for i in range(9):
        i=i + int(inputRecords)
        resultTemplate={
               "buttons": [
                {
                  "set_attributes": {
                    "imageInput": "some value",
                    "upperText": "another value",
                    "lowerText": "lower text value"
                  },
                  "block_names": [
                    "Routing"
                  ],
                  "type": "show_block",
                  "title": "customise"
                },
                {
                  "type": "element_share"
                }
              ]
            }
        #print(i)
        #print(exampleUrlList[i])
        imageInput, upperText, lowerText = splitLink(exampleUrlList[i])
        #print(imageInput, upperText, lowerText)
        if upperText !=" ":
            resultTemplate['title']= upperText
            resultTemplate['subtitle']= lowerText
        else:
            resultTemplate['title']= lowerText
            resultTemplate['subtitle']= upperText
        resultTemplate['image_url'] = exampleUrlList[i]
            
        resultTemplate["buttons"][0]["set_attributes"]["imageInput"]= imageInput
        resultTemplate["buttons"][0]["set_attributes"]["upperText"]= upperText
        resultTemplate["buttons"][0]["set_attributes"]["lowerText"]= lowerText
        #print(resultTemplate)
        galleryResponse['messages'][0]['attachment']['payload']['elements'].append(resultTemplate)
        #print(galleryResponse)
        
    moreResult= {'title':"want to see more",
           "buttons": [
            {
              "set_attributes": {
                "inputRecords": i+1,
              },
              "block_names": [
                "imageJson"
              ],
              "type": "show_block",
              "title": "show more"
            }
          ]
        }
    galleryResponse['messages'][0]['attachment']['payload']['elements'].append(moreResult)
    return jsonify(galleryResponse)


@app.route('/generateMEME', methods=['POST', 'GET'])
def generateMeme():
    imageInput = request.args.get('imageInput')
    upperText = request.args.get('upperTextInput')
    lowerText = request.args.get('lowerTextInput')
    print(imageInput,upperText,lowerText)
    print( imageInput+upperText+"/"+lowerText+ ".jpg")
    print(type( imageInput+upperText+"/"+lowerText+ ".jpg"))
    result = {
      "messages": [
        {
          "attachment": {
            "type": "image",
            "payload": {
              "url": imageInput+upperText+"/"+lowerText+ ".jpg"
            }
          }
        }
      ]
    }
    return jsonify(result)
if __name__ == '__main__':
  app.debug = True
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port = port)
"""
Google Api인 Googletrans를 이용하여 번역기 구현
"""

#%%
import googletrans

# %%
translate = googletrans.Translator()
# 무작위 기사를 가져와 테스트
str1 = '''The Taliban said Tuesday that they were "not allowing the evacuation of Afghans anymore" and warned that the US must stick to next week's deadline to pull out, as a frantic Western evacuation operation at Kabul airport picked up pace.
The announcement came as US President Joe Biden made clear he aims to stick with his August 31 deadline to withdraw troops from Afghanistan -- as long as the Taliban does not disrupt ongoing evacuation operations or airport access. Top American allies have already called for an extension in order to fly more people out.
Taliban spokesman Zabiullah Mujahid told a press conference Tuesday that while foreign nationals could continue traveling to the airport, the huge crowds of Afghans that have gathered there in recent days should return home and would not face reprisals from the country's new rulers.
"The road, which goes to the airport, is blocked. Afghans cannot take that road to go to the airport, but foreign nationals are allowed to take that road to the airport," Mujahid said.
"We are not allowing the evacuation of Afghans anymore and we are not happy with it either," he added.
The doctors and academics of Afghanistan "should not leave this country, they should work in their own specialist areas," Mujahid added. "They should not go to other countries, to those Western countries."
Asked about the statement from the Taliban, White House press secretary Jen Psaki said that should not impact Afghans who were prioritized by the US to leave the country. "No. That is not how you should read it," Psaki said.
"Our expectation, which we have also conveyed to the Taliban, is that they should be able to get to the airport," she later added.
Many of those fleeing the country since the Taliban took over have been educated people, especially women. The last time the Taliban ruled, women were banned from working and forbidden to attend schools and universities.
Mujahid also gave reassurances that foreign embassies and aid agencies would remain open.
But experts remain dubious of such pledges amid reports of human rights abuses and concerns that the situation will deteriorate further once most of the international community leaves the country.
G7 leaders were meeting Tuesday in the first such international forum since the Taliban toppled the internationally-backed Afghan government more than a week ago.
They have called on the Taliban to guarantee safe passage for all those wishing to leave Afghanistan after August 31, UK Prime Minister Boris Johnson said Tuesday, describing this as the G7's "number one condition" for the Taliban.
"The number one condition we are setting as G7 is that they've got to guarantee right the way through -- through August 31 and beyond -- safe passage for those who want to come out," Johnson said after the virtual meeting of G7 leaders.'''
result1 = translate.translate(str1,src='en',dest='ko').text

# %%
result1

#%%
googletrans.__version__



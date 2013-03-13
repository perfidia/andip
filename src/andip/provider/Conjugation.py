#-*- coding: utf-8 -*-
'''
Created on 13-03-2013

@author: Mateusz
'''

class Conjugation(object):
        
    def get_word_present(self,conj_type, forma, liczba, osoba, base_word):
        new_end =  conjugation[conj_type]['time'][forma][liczba][osoba]
        return base_word.replace(str(conjugation[conj_type]['end']), str(new_end))
    
    def get_word_past(self,conj_type, forma, liczba, rodzaj, osoba, base_word):
        new_end =  conjugation[conj_type]['time'][forma][liczba][rodzaj][osoba]
        return  base_word.replace(conjugation[conj_type]['end'], new_end)
        
        
conjugation = {
               'I' : {
                      'end' : 'ać',
                      'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'am',
                                                                       'druga': 'asz',
                                                                       'trzecia': 'a'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'amy',
                                                                        'druga' : 'acie',
                                                                        'trzecia' : 'ają'
                                                                }
                                                       }
                                }
                },
               'II' : {
                       'end' : 'eć',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'em',
                                                                       'druga': 'esz',
                                                                       'trzecia': 'e'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'emy',
                                                                        'druga' : 'ecie',
                                                                        'trzecia' : 'eją'
                                                                }
                                                       }
                                }
                },
               'III' : {
                        'end' : 'eć',
                        'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'eję',
                                                                       'druga': 'ejesz',
                                                                       'trzecia': 'eje'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ejemy',
                                                                        'druga' : 'ejecie',
                                                                        'trzecia' : 'eją'
                                                                }
                                                       }
                                }
                },
               'IV' : {
                       'end' : 'ować',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'uję',
                                                                       'druga': 'ujesz',
                                                                       'trzecia': 'uje'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ujemy',
                                                                        'druga' : 'ujecie',
                                                                        'trzecia' : 'ują'
                                                                }
                                                       }
                                ,
                                'czas przeszly' : {
                                                   'pojedyncza' : {
                                                                   'meski' : {
                                                                                    'pierwsza' : 'owałem',
                                                                                    'druga' : 'owałeś',
                                                                                    'trzecia' : 'ował'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'owałam',
                                                                                    'druga' : 'owałaś',
                                                                                    'trzecia' : 'owała'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'pierwsza' : 'owałom',
                                                                                    'druga' : 'owałoś',
                                                                                    'trzecia' : 'owało'
                                                                               }
                                                                  },
                                                   'mnoga' : {
                                                                    'meski' : {
                                                                                    'pierwsza' : 'owaliśmy',
                                                                                    'druga' : 'owaliście',
                                                                                    'trzecia' : 'owali'
                                                                              },
                                                                   'zenski' : {
                                                                                    'pierwsza' : 'owałyśmy',
                                                                                    'druga' : 'owałyście',
                                                                                    'trzecia' : 'owały'
                                                                               },
                                                                   'nijaki' : {
                                                                                    'pierwsza' : 'owałyśmy',
                                                                                    'druga' : 'owałyście',
                                                                                    'trzecia' : 'owały'
                                                                               }
                                                              }
                                        }
                                 }
                },
                'Va' : {
                        'end' : 'nąć',
                        'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'nę',
                                                                       'druga': 'niesz',
                                                                       'trzecia': 'nie'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'niemy',
                                                                        'druga' : 'niecie',
                                                                        'trzecia' : 'ną'
                                                                }
                                                       }
                                }
                },
                'Vb' : {
                        'end' : 'nąć',
                        'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'nę',
                                                                       'druga': 'niesz',
                                                                       'trzecia': 'nie'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'niemy',
                                                                        'druga' : 'niecie',
                                                                        'trzecia' : 'ną'
                                                                }
                                                       }
                                }
                },
                'Vc' : {
                        'end' : 'nąć',
                        'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'nę',
                                                                       'druga': 'niesz',
                                                                       'trzecia': 'nie'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'niemy',
                                                                        'druga' : 'niecie',
                                                                        'trzecia' : 'ną'
                                                                }
                                                       }
                                }
                },
               'VIa' : {
                       'end' : 'ić',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ę',
                                                                       'druga': 'isz',
                                                                       'trzecia': 'i'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'imy',
                                                                        'druga' : 'icie',
                                                                        'trzecia' : 'ą'
                                                                }
                                                       }
                                } 
                },
               'VIb' : {
                       'end' : 'yć',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ę',
                                                                       'druga': 'ysz',
                                                                       'trzecia': 'y'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ymy',
                                                                        'druga' : 'ycie',
                                                                        'trzecia' : 'ą'
                                                                }
                                                       }
                                } 
                },
               'VIIa' : {
                       'end' : 'eć',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ę',
                                                                       'druga': 'isz',
                                                                       'trzecia': 'i'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'imy',
                                                                        'druga' : 'icie',
                                                                        'trzecia' : 'ą'
                                                                }
                                                       }
                                } 
                },
               'VIIb' : {
                       'end' : 'eć',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ę',
                                                                       'druga': 'ysz',
                                                                       'trzecia': 'y'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ymy',
                                                                        'druga' : 'ycie',
                                                                        'trzecia' : 'ą'
                                                                }
                                                       }
                                } 
                },
               'VIIIa' : {
                       'end' : 'ywać',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'uję',
                                                                       'druga': 'ujesz',
                                                                       'trzecia': 'uje'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ujemy',
                                                                        'druga' : 'ujecie',
                                                                        'trzecia' : 'ują'
                                                                }
                                                       }
                                } 
                },
               'VIIIb' : {
                       'end' : 'iwać',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'uję',
                                                                       'druga': 'ujesz',
                                                                       'trzecia': 'uje'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ujemy',
                                                                        'druga' : 'ujecie',
                                                                        'trzecia' : 'ują'
                                                                }
                                                       }
                                } 
                },
               'IX' : {
                       'end' : 'ać',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ę',
                                                                       'druga': 'esz',
                                                                       'trzecia': 'e'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'emy',
                                                                        'druga' : 'ecie',
                                                                        'trzecia' : 'ą'
                                                                }
                                                       }
                                } 
                },
               'Xa' : {
                       'end' : 'ć',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ję',
                                                                       'druga': 'jesz',
                                                                       'trzecia': 'je'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'jemy',
                                                                        'druga' : 'jecie',
                                                                        'trzecia' : 'ją'
                                                                }
                                                       }
                                } 
                },
               'Xb' : {
                       'end' : 'ać',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'eję',
                                                                       'druga': 'ejesz',
                                                                       'trzecia': 'eje'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'ejemy',
                                                                        'druga' : 'ejecie',
                                                                        'trzecia' : 'eją'
                                                                }
                                                       }
                                } 
                },
               'Xc' : {
                       'end' : 'ać',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'mę',
                                                                       'druga': 'miesz',
                                                                       'trzecia': 'mie'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'miemy',
                                                                        'druga' : 'miecie',
                                                                        'trzecia' : 'mą'
                                                                }
                                                       }
                                } 
                },
               'XI' : {
                       'end' : 'ć',
                       'time' : {
                                'czas terazniejszy' : {
                                                       'pojedyncza' : {
                                                                       'pierwsza' : 'ę',
                                                                       'druga': 'esz',
                                                                       'trzecia': 'e'
                                                                       },
                                                       'mnoga' : {
                                                                        'pierwsza' : 'emy',
                                                                        'druga' : 'ecie',
                                                                        'trzecia' : 'ą'
                                                                }
                                                       }
                                } 
                },
               
}
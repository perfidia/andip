#-*- coding: utf-8 -*-
'''
Created on 13-03-2013

@author: Mateusz
'''

class Schema(object):
        
    def get_word_present(self,conj_type, forma, liczba, osoba, base_word):
        new_end = conjugation[conj_type]['forma'][forma][liczba][osoba]
        return base_word.replace(str(conjugation[conj_type]['koncowka']), str(new_end))
    
    def get_word_past(self,conj_type, forma, liczba, rodzaj, osoba, base_word):
        new_end = conjugation[conj_type]['forma'][forma][liczba][rodzaj][osoba]
        return  base_word.replace(conjugation[conj_type]['koncowka'], new_end)
        
        
conjugation = {
               'I' : {
                      'koncowka' : 'ać',
                      'forma' : {
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
                       'koncowka' : 'eć',
                       'forma' : {
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
                        'koncowka' : 'eć',
                        'forma' : {
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
                       'koncowka' : 'ować',
                       'forma' : {
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
                        'koncowka' : 'nąć',
                        'forma' : {
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
                        'koncowka' : 'nąć',
                        'forma' : {
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
                        'koncowka' : 'nąć',
                        'forma' : {
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
                       'koncowka' : 'ić',
                       'forma' : {
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
                       'koncowka' : 'yć',
                       'forma' : {
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
                       'koncowka' : 'eć',
                       'forma' : {
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
                       'koncowka' : 'eć',
                       'forma' : {
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
                       'koncowka' : 'ywać',
                       'forma' : {
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
                       'koncowka' : 'iwać',
                       'forma' : {
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
                       'koncowka' : 'ać',
                       'forma' : {
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
                       'koncowka' : 'ć',
                       'forma' : {
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
                       'koncowka' : 'ać',
                       'forma' : {
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
                       'koncowka' : 'ać',
                       'forma' : {
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
                       'koncowka' : 'ć',
                       'forma' : {
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

adjective_schema = {
	'y': {
		'przypadek': {
			'mianownik': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'y',
							'ż': 'a',
							'n': 'e'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'i',
							'nm': 'e'
						}
					}
				}
			}, # end mianownik
			'dopełniacz': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'ego',
							'ż': 'ej',
							'n': 'ego'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'ych', 
							'nm': 'ych'
						}
					}
				}
			}, # end dopełniacz
			'celownik': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'emu',
							'ż': 'ej',
							'n': 'emu'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'ym', 
							'nm': 'ym'
						}
					}
				}
			}, # end celownik
			'biernik': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'ego',
							'ż': 'ą',
							'n': 'e'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'ych', 
							'nm': 'e'
						}
					}
				}
			}, # end biernik
			'narzędnik': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'ym',
							'ż': 'ą',
							'n': 'ym'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'ymi', 
							'nm': 'ymi'
						}
					}
				}
			}, # end narzędnik
			'miejscownik': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'ym',
							'ż': 'ej',
							'n': 'ym'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'ych', 
							'nm': 'ych'
						}
					}
				}
			}, # end miekscownik
			'wołacz': {
				'liczba': {
					'pojedyncza': {
						'rodzaj': {
							'm': 'y',
							'ż': 'a',
							'n': 'e'
						}
					},
					'mnoga': {
						'rodzaj': {
							'm': 'i', 
							'nm': 'e'
						}
					}
				}
			} # end wołacz
		} # end przypadek
	} # end y
}
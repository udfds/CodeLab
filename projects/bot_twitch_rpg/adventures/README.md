# 


### Adventures template schema:
- Propriedades que começam o caracterer '_' são opcionais
- 

---

#### Objeto 'adventure'

Object que descreve como uma aventura

```
    "adventure": {
        "adventure_title": "string",
        "adventure_id": "string",
        "_image_url": "string",
        "_requires": [ "string" ]
    },
    ...
```

adventure.adventure_title
- Propriedade que nomeia uma aventura
- Notas:
    - Valor obrigatorio
    - Tamanho maximo sugerido: 255

adventure.adventure_id
- Propriedade que identifica uma aventura
- Notas:
    - Valor obrigatorio e unico
    - Tamanho maximo sugerido: 255
    - Padrão sugerido: NOME_DA_AVENTURA

adventure._image_url
- Propriedade que identifica uma imagem a ser utilizada na aventura
- Notas:
    - Valor opcional 
    - Verificar o conteudo e direitos autorais antes de utilizar a imagem

adventure._requires
- Lista de requerimentos para iniciar a aventura
- Cada item da lista é o id de um evento global
- Notas:
    - Lista opcional

---

#### Objeto '_settings'

Object que descreve a configuração padrão da aventura

```
    ...
    "_settings": {
        "_default_transition_time": "interge",
        "_default_voting_time": "interge",
        "_default_death_scenes": "interge"
    },
    ...
```

_settings._default_transition_time
- Propriedade que define o tempo (segundos) ate troca de cena
- Notas:
    - Propriedade opcional
    - Valor inicial: 60 (segundos)

_settings._default_voting_time
- Propriedade que define o tempo (segundos) para a votação
- Notas:
    - Propriedade opcional
    - Valor inicial: 60 (segundos)

_settings._default_death_scenes
- Define a cena que vai ser apresentada em caso de morte do personagem
- Notas:
    - Propriedade opcional
    - Tamanho maximo sugerido: 255
    - Valor inicial: "\_ENDGAME\_"

---

#### Objeto '_artifacts'

Lita de objetos que descreve um artefato, item, presente na aventura

```
    ...
    "_artifacts": [
        {
            "name": "string",
            "global_event_id": "string",
            "_set": {
                ...
            }
        }
    ],
    ...
```

_artifacts[index].name
- Propriedade que define o nome de um artefato
- Notas:
    - Propriedade obrigatoria
    - Tamanho maximo sugerido: 255

_artifacts[index].global_event_id
- Propriedade que define um evento unico para o personagem
- Notas:
    - Propriedade obrigatoria e unico
    - Tamanho maximo sugerido: 255
    - Padrão sugerido: NOME_UNICO

_artifacts[index]._set
- Objeto que descreve efeitos a ser aplicado ao personagem
- Notas:
    - Objeto opcional

---

#### Objeto '_set'

Objeto que descreve um efeito a ser aplicado ao personagem

```
    ...
    "_set": {
        "_life": "string",
        "_defense": "string",
        "_attack": "string",
        "_power": "string",
        "_gold": "string",
        "_luck": "string"
    }
    ...
```

_set: _life, _defense, _attack, _power, _gold, _luck
- Propriedade que define uma alteração na (vida, defesa, ataque, poder, gold, sorte) do personagem

Notas:
- Propriedade opcional
- Formato: 'operação matematica' + 'numero inteiro'
    - Exemplos:  "+1", "-2", "*3", "/4", "=5"
- Qualquer valor fora do padrão é ignorado

---

#### Objeto '_events'

Lita de objetos que descreve um evento, local, presente na aventura
Essa lista de eventos não representa um eventos globais

```
    ...
    "_events": [
        {
            "event_id": "string",
            "_gain": { 
                ... 
            },
            "_lost": { 
                ... 
            },
            "_set": { 
                ... 
            }
        }
    ],
    ...
```

_events[index].event_id
- Propriedade que identifica um evento
- Notas:
    - Propriedade obrigatoria
    - Tamanho maximo sugerido: 255
    - Padrão sugerido: NOME_UNICO

_events[index]._gain
- Propriedade que representa eventos e artefatos recebido devido ao evento
- Notas:
    - Propriedade opcional

_events[index]._lost
- Propriedade que representa eventos e artefatos perdido devido ao evento
- Notas:
    - Propriedade opcional

_events[index]._set
- Objeto que descreve um efeito a ser aplicado ao personagem

---

#### Objeto '_gain' & _lost

TODO

```
    ...
    "_gain": {
        "_events_ids": [ "string" ], 
        "_artifacts_ids": [ "string" ],
        "_global_event_id": [ "string" ]
    },

    "_lost": {
        "_events_ids": [ "string" ], 
        "_artifacts_ids": [ "string"],
        "_global_event_id": [ "string" ]
    },
    ...
```
_gain._events_ids & _lost._events_ids
- TODO

_gain._artifacts_ids & _lost._artifacts_ids
- TODO

_gain._global_event_id & _lost._global_event_id
- TODO

---

#### Objeto 'scenes'

TODO

```
    ...
    "scenes": [
        {
            "scene_id": "string",
            "next_scene_id": "string",
            "_text": "string",
            "_image_url": "string",
            "_requires": [
                ...
            ],
            "_actions": [ ... ]
        }
    ]
```
scenes[index].scene_id
- TODO

scenes[index].next_scene_id
- TODO

scenes[index]._text
- TODO

scenes[index]._image_url
- TODO

scenes[index]._requires
- TODO

scenes[index]._actions
- TODO


---

#### Objeto '_actions'

TODO

```
    ...
     "_actions": [
        {
            "text": "string",
            "_requires": [ ... ],
            "_event_id": "string",
            "_test": {
                ...
            }
        }
    ]
    ...
```
_actions[index].text
- TODO

_actions[index]._requires
- TODO

_actions[index]._event_id
- TODO

_actions[index]._test
- TODO

---

#### Objeto '_test'

TODO

```
    ...
    "_test": {
        "property": "string",
        "event_sucess_id": "string",
        "event_fail_id": "string"
    }
    ...
```
_test.property
- TODO

_test.event_sucess_id
- TODO

_test.event_fail_id
- TODO

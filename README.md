# DBSE_Project-Task_Personalization-
Contextual similarity between an exercise task, and
a given section or sections of a specific course instruction artifact
is an essential relationship necessary for both the acquisition
of respective knowledge, and testing of the degree to which
a student has a given concept. Thus, it becomes evident, the
challenge of maintaining this relationship during the composition
of exercise tasks for many students. In our peculiar context,
based on Structured Query Language (SQL) skill acquisition,
it became important to reduce the frequency of exercise task
reuse in SQLValidator, as high frequency of reuse increases
the likelihood of task solution sharing among student, and
eventual poor knowledge acquisition. Also in our context of
use, it is requiring that tasks further be semantically similar,
a requirement centered on the query language feature being
tested by the task. To this end, we have developed an automatic
task generation system for Structured Query Language based
exercise tasks. To realize the system, we first perform parts
of speech tagging on manually crafted tasks, and from these
generate contextually similar tasks using Bag-of-words(BOW)
language model, Bidirectional Encoder Representations from
Transformers (BERT) language model, and the cosine similarity
metric. Evaluation shows that the BERT model performed better,
reaching a precision value of 0.7142, and an accuracy of 0.8,
compared to the cosine similarity strategy which achieved a
precision value of 0.67, and an accuracy of 0.7. These results
justify our strategy of automatically generating exercise tasks
using the above-mentioned models

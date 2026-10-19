# PA 2
from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ' '

    f_name = document.getElementById('fname').value.title().strip()
    l_name = document.getElementById('lname').value.title().strip()
    grade_seven = {'austin maneja', 'antonio manalo', 'lincoln del rosario'}
    grade_eight = {'jayden ambata', 'summer atienza', 'elijah briones'}
    grade_nine = {'azriela sangco', 'theos tomas', 'precious irinco'}
    grade_ten = {'shiloh briones', 'nicole manalang', 'dapne mariano'}

    # Combining all the sets
    club_members = grade_seven | grade_eight | grade_nine | grade_ten
    # Combining the name
    full_name = f_name + " " + l_name
    # Adding the given name
    club_members.add(full_name)

    display(club_members, target="div1")
    display(f"The club has {len(club_members)} members.", target="div1")


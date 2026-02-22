from pyscript import document

def check_intramurals(event=None):
    olr = document.querySelector("input[name='OLR']:checked")
    mc = document.querySelector("input[name='MC']:checked")
    grade = document.getElementById("Grade").value
    section = document.getElementById("Section").value

    output = document.getElementById("output")
    output.innerHTML = ""

    olr = olr.value if olr else ""
    mc = mc.value if mc else ""

    valid_sections = ["Topaz", "Emerald", "Ruby", "Sapphire"]

    eligible = (
        olr == "Yes"
        and mc == "Yes"
        and grade in ["7", "8", "9", "10"]
        and section in valid_sections
    )

    if eligible:
        teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]
        team = teams[valid_sections.index(section)]

        output.innerHTML = (
            "<b>Congratulations!</b><br>"
            "You are eligible to join the Intramurals.<br>"
            f"<b>Assigned Team:</b> {team}"
        )
    else:
        if olr != "Yes":
            output.innerHTML += "Please register online.<br>"
        if mc != "Yes":
            output.innerHTML += "Please secure a medical clearance.<br>"
        if grade not in ["7", "8", "9", "10"]:
            output.innerHTML += "You must be in grades 7–10 to join.<br>"
        if section not in valid_sections:
            output.innerHTML += "Please select a valid section.<br>"
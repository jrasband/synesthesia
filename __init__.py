from aqt import mw
from aqt import gui_hooks

# Add a border to cards based on the config
def prepare(html, card, context):
    added_script = ""
    # Load json configuration
    config = mw.addonManager.getConfig(__name__)
    data_dict = config["tag-color-weight"]
    tag_dict = {tag:data_dict[tag] for tag in card.note().tags if tag in data_dict.keys()}
    if len(tag_dict) != 0:
        max_tag = max(tag_dict, key=lambda tag: tag_dict[tag]["weight"])
        max_color = tag_dict[max_tag]["color"]
        added_script = f"""
<script>
document.body.style.border = "10px solid {max_color}";
</script>"""

    return html + added_script
gui_hooks.card_will_show.append(prepare)
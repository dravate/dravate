from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class CodeBlock(StructBlock):
    code = StructBlock([
                ('language', ChoiceBlock(choices=[
                    ('python', 'Python'),
                    ('javascript', 'Javascript'),
                     ('htmlmixed', 'HTML'),
                     ('css', 'CSS'),
                    ('shell', 'Shell'),
                ])),
               ('text', TextBlock()),
            ])
    class Meta:
         icon="code"
         template = "blocks/code_block.html"


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"




class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"




class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"



# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """
    code = CodeBlock()
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow", template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        max_width=800,
        max_height=400,
        template="blocks/embed_block.html"
    )
# for instructor only 

class ProfileBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
      
    image = ImageChooserBlock(required=True)
    firstname = CharBlock(required=True) 
    lastname  = CharBlock(required=False)
    title  = CharBlock(required=False)
    linkedin  = CharBlock(required=False)
    short_profile  = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/profile_image_block.html"



# Instructore - used for training/courses pages
class TrainerBlock(StreamBlock):
      profile = ProfileBlock()
      


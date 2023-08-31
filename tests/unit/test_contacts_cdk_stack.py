import aws_cdk as core
import aws_cdk.assertions as assertions

from contacts_cdk.contacts_cdk_stack import ContactsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in contacts_cdk/contacts_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ContactsCdkStack(app, "contacts-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

import React, { Component, Fragment } from 'react';
import { Editor } from 'slate-react';
import { Value } from 'slate';
import { BoldMark, ItalicMark, FormatToolbar } from './index';
import Icon from 'react-icons-kit';
import { bold } from 'react-icons-kit/feather/bold';
import { italic } from 'react-icons-kit/feather/italic';
import { code } from 'react-icons-kit/feather/code';
import { list } from 'react-icons-kit/feather/list';
import { underline } from 'react-icons-kit/feather/underline';
import { listNumbered } from 'react-icons-kit/icomoon/listNumbered';
import { ic_format_quote } from 'react-icons-kit/md/ic_format_quote';
import { ic_looks_one } from 'react-icons-kit/md/ic_looks_one';
import { ic_looks_two } from 'react-icons-kit/md/ic_looks_two';

const initialValue = Value.fromJSON({
    document: {
        nodes: [
            {
                object: 'block',
                type: 'paragraph',
                nodes: [
                    {
                        object: 'text',
                        leaves: [
                            {
                                text: 'Rich text editor',
                            },
                        ],
                    },
                ],
            },
        ],
    },
});

export default class TextEditor extends Component {

    state = {
        value: initialValue,
    };

    /**
     * Action: On change value, set a state
     */
    onChange = ({ value }) => {
        this.setState({ value })
    };

    /**
     * Action: On key press, apply a effect
     */
    onKeyDown = (event, change) => {

        // Cancel the event, case the key control is not pressed
        if (!event.ctrlKey) {
            return;
        }

        // Cancel the event effect
        event.preventDefault();

        switch (event.key) {
            case 'b':
                change.toggleMark('bold');
                return true;

            case 'i':
                change.toggleMark('italic');
                return true;

            case 'c':
                change.toggleMark('code');
                return true;

            case 'l':
                change.toggleMark('list');
                return true;

            case 'u':
                change.toggleMark('underline');
                return true;

            case '1':
                change.toggleMark('heading-one');
                return true;

            case '2':
                change.toggleMark('heading-two');
                return true;

            case 'n':
                change.toggleMark('numbered-list');
                return true;

            case 'p':
                change.toggleMark('paragraph');
                return true;

            case 'q':
                change.toggleMark('block-quote');
                return true;

            default:
                return;
        }
    };

    /**
     * Action: On mark click, apply a effect
     */
    onMarkClick = (event, type) => {
        // Cancel the event effect
        event.preventDefault();

        // Load the target effect
        const { value } = this.state;
        const change = value.change().toggleMark(type);

        // Apply the target effect
        this.onChange(change);
    };

    /**
     * Render: Build and return the target element structure
     */
    renderMark = props => {
        switch (props.mark.type) {
            case 'bold':
                return <BoldMark {...props} />;

            case 'italic':
                return <ItalicMark {...props} />;

            case 'code':
                return <code {...props.attribute}>{props.children}</code>;

            case 'list':
                return (<ul {...props.attribute}> <li>{props.children}</li> </ul>);

            case 'underline':
                return <u {...props.attribute}>{props.children}</u>

            case 'heading-one':
                return <h1 {...props.attributes}>{props.children}</h1>

            case 'heading-two':
                return <h2 {...props.attributes}>{props.children}</h2>

            case 'numbered-list':
                return <ol {...props.attributes}>{props.children}</ol>

            case 'block-quote':
                return <blockquote {...props.attributes}>{props.children}</blockquote>
        }
    };

    /**
     * Render: BUild and return the component structure
     */
    render() {
        return (
            <Fragment>
                <FormatToolbar>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'bold')}>
                        <Icon icon={bold}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'italic')}>
                        <Icon icon={italic}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'code')}>
                        <Icon icon={code}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'list')}>
                        <Icon icon={list}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'underline')}>
                        <Icon icon={underline}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'heading-one')}>
                        <Icon icon={ic_looks_one}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'heading-two')}>
                        <Icon icon={ic_looks_two}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'numbered-list')}>
                        <Icon icon={listNumbered}></Icon>
                    </button>
                    <button className="tooltip-icon-button"
                        onPointerDown={(e) => this.onMarkClick(e, 'block-quote')}>
                        <Icon icon={ic_format_quote}></Icon>
                    </button>
                </FormatToolbar>

                <Editor
                    value={this.state.value}
                    onChange={this.onChange}
                    onKeyDown={this.onKeyDown}
                    renderMark={this.renderMark}
                />
            </Fragment>
        );
    }

}

// Copyright (c) 2019, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the MIT license found in the
// LICENSE file in the "hack" directory of this source tree.

use std::fmt::Debug;

use crate::trivia_kind::TriviaKind;

pub trait LexableTrivia: Clone + Debug {
    type Trivium: LexableTrivium;

    fn is_empty(&self) -> bool;
    fn has_kind(&self, kind: TriviaKind) -> bool;
    fn push(&mut self, trivium: Self::Trivium);
    fn extend(&mut self, other: Self);

    #[inline]
    fn make_whitespace(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_whitespace(offset, width)
    }
    #[inline]
    fn make_eol(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_eol(offset, width)
    }
    #[inline]
    fn make_single_line_comment(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_single_line_comment(offset, width)
    }
    #[inline]
    fn make_fallthrough(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_fallthrough(offset, width)
    }
    #[inline]
    fn make_fix_me(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_fix_me(offset, width)
    }
    #[inline]
    fn make_ignore(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_ignore(offset, width)
    }
    #[inline]
    fn make_ignore_error(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_ignore_error(offset, width)
    }
    #[inline]
    fn make_extra_token_error(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_extra_token_error(offset, width)
    }
    #[inline]
    fn make_delimited_comment(offset: usize, width: usize) -> Self::Trivium {
        Self::Trivium::make_delimited_comment(offset, width)
    }
}

pub trait LexableTrivium: Clone + PartialEq + Debug {
    fn make_whitespace(offset: usize, width: usize) -> Self;
    fn make_eol(offset: usize, width: usize) -> Self;
    fn make_single_line_comment(offset: usize, width: usize) -> Self;
    fn make_fallthrough(offset: usize, width: usize) -> Self;
    fn make_fix_me(offset: usize, width: usize) -> Self;
    fn make_ignore(offset: usize, width: usize) -> Self;
    fn make_ignore_error(offset: usize, width: usize) -> Self;
    fn make_extra_token_error(offset: usize, width: usize) -> Self;
    fn make_delimited_comment(offset: usize, width: usize) -> Self;
    fn kind(&self) -> TriviaKind;
    fn width(&self) -> usize;
}
